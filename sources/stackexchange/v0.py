import argparse
import io
import os
import re
import sys
from contextlib import ExitStack
from io import BytesIO
from pathlib import Path
from typing import Any, BinaryIO, Dict, Iterator, Optional

import libarchive
import py7zr
import pyarrow as pa
import pyarrow.parquet as pq
from libarchive.entry import ArchiveEntry
from lxml import etree
from tqdm import tqdm

os.environ["PYTHONBREAKPOINT"] = "ipdb.set_trace"


def get_7z_uncompressed_size(sz_path, entry_name):
    with py7zr.SevenZipFile(sz_path, mode="r") as z:
        for entry in z.list():
            if entry.filename == entry_name:
                return entry.uncompressed
        raise FileNotFoundError(f"File {entry_name} not found in archive {sz_path}")


def stream_xml_from_7z(
    archive_path: str, filename: str, target_xpath: str = "//*", block_size: int = 8192
) -> Iterator[etree._Element]:
    """
    Stream XML nodes from a file within a 7z archive, parsing them lazily.

    Args:
        archive_path (str): Path to the 7z archive
        filename (str): Name of the XML file within the archive
        target_xpath (str, optional): XPath expression to filter nodes. Defaults to "//*".
        block_size (int, optional): Size of blocks to read. Defaults to 8192.

    Yields:
        lxml.etree._Element: XML nodes matching the target_xpath

    Raises:
        FileNotFoundError: If archive or file within archive is not found
        ValueError: If file is not valid XML
    """
    # Initialize the XML parser that will receive chunks of data
    parser = etree.XMLPullParser(events=("end",), recover=True)

    with ExitStack() as stack:
        archive = stack.enter_context(libarchive.file_reader(archive_path))
        # Find the target file in the archive
        for entry in archive:
            if entry.pathname != filename:
                continue

            archive_name = os.path.basename(archive_path)
            pbar = tqdm(
                total=get_7z_uncompressed_size(archive_path, filename),
                desc=f"Bytes {archive_name}::{filename}",
                unit="B",
                unit_scale=True,
            )
            prev_line = b""
            for chunk in entry.get_blocks(block_size):
                pbar.update(len(chunk))
                first_seg, *segments = re.split(b"\r*\n|\r", chunk)
                yield prev_line + first_seg
                yield from segments[:-1]
                prev_line = segments[-1]


def process_file(
    archive_path: str,
    output_dir: str,
    entry_name: str,
    batch_size: int = 100_000,
    block_size: int = 8192,
):
    entry_prefix, _ = os.path.basename(entry_name.lower()).split(".", 1)
    output_dir = os.path.join(output_dir, entry_prefix)
    archive_name = os.path.basename(archive_path)

    os.makedirs(output_dir, exist_ok=True)
    data = []
    schema = None

    with ExitStack() as stack:
        xml_elements = stream_xml_from_7z(archive_path, entry_name, block_size=block_size)
        files_pbar = tqdm(desc=f"Files {archive_name}::{entry_name}")
        elements_pbar = tqdm(xml_elements, desc=f"Rows {archive_name}::{entry_name}")

        for row in elements_pbar:
            if not row.strip().startswith(b"<row"):
                continue

            row = etree.fromstring(row)

            if not row.attrib:
                continue

            data.append(dict(row.attrib))

            if schema is None:
                schema = pa.Table.from_pylist(data).schema

            if len(data) >= batch_size:
                table = pa.Table.from_pylist(data, schema=schema)
                pq.write_table(
                    table,
                    os.path.join(output_dir, f"{entry_prefix}_{files_pbar.n:06d}.parquet"),
                )
                data = []
                files_pbar.update(1)
        # Write any remaining data

        if data:
            table = pa.Table.from_pylist(data, schema=schema)
            pq.write_table(
                table,
                os.path.join(output_dir, f"{entry_prefix}_{files_pbar.n:06d}.parquet"),
            )
            files_pbar.update(1)


def main():
    parser = argparse.ArgumentParser(description="Convert Stack Exchange 7z XML dumps to Parquet format")
    parser.add_argument("archive_path", help="Path to the 7z archive")
    parser.add_argument("output_dir", help="Directory where Parquet files will be saved")
    parser.add_argument(
        "--batch-size", type=int, default=100000, help="Number of rows to process at once (default: 100000)"
    )
    parser.add_argument("--block-size", type=int, default=8192, help="Size of blocks to read (default: 8192)")

    args = parser.parse_args()

    if os.path.isdir(args.archive_path):
        archive_paths = [
            os.path.join(args.archive_path, p) for p in os.listdir(args.archive_path) if p.endswith("7z")
        ]
        output_paths = [os.path.join(args.output_dir, os.path.basename(p)) for p in archive_paths]
    else:
        archive_paths = [args.archive_path]
        output_paths = [args.output_dir]

    for archive_path, output_path in tqdm(
        zip(archive_paths, output_paths), desc="Archives", total=len(archive_paths)
    ):
        for entry_name in ["Posts.xml", "Comments.xml"]:
            process_file(
                archive_path=archive_path,
                output_dir=output_path,
                entry_name=entry_name,
                batch_size=args.batch_size,
                block_size=args.block_size,
            )


if __name__ == "__main__":
    main()
