from dataclasses import dataclass
from typing import List, Optional

from omegaconf import MISSING

from dolma.cli import BaseCli, field, print_config
from dolma.cli.shared import WorkDirConfig
from dolma.core.errors import DolmaConfigError
from dolma.core.loggers import get_logger
from dolma.core.paths import glob_path
from dolma.core.runtime import create_and_run_tagger


@dataclass
class TaggerConfig:
    documents: List[str] = field(
        default=[],
        help="One or more document paths to process; Can be either local or S3 paths. Globs are supported.",
    )
    destination: Optional[List[str]] = field(
        default=None,
        nargs="*",
        help=(
            "Destination paths to save the outputs; should match the number of document paths. "
            "If not provided, destination will be derived from the document path."
        ),
    )
    taggers: List[str] = field(
        default=[],
        help="List of taggers to run.",
    )
    experiment: str = field(
        default=MISSING,
        help="Name of the experiment.",
    )
    processes: int = field(
        default=1,
        help="Number of parallel processes to use.",
    )
    debug: bool = field(
        default=False,
        help="Whether to run in debug mode.",
    )
    work_dir: Optional[WorkDirConfig] = field(
        default=WorkDirConfig(), help="Configuration for temporary work directories."
    )


class TaggerCli(BaseCli):
    CONFIG = TaggerConfig

    @classmethod
    def run(cls, parsed_config: TaggerConfig):
        logger = get_logger("tagger")

        metadata = parsed_config.work_dir.output if parsed_config.work_dir else None
        documents = [str(p) for p in parsed_config.documents]
        taggers = [str(p) for p in parsed_config.taggers]

        # perform some path validation to make sure we don't call the mixer with invalid config
        total_matching_documents = 0
        for document in documents:
            current_matching_documents = sum(1 for _ in glob_path(document))
            if current_matching_documents == 0:
                # only raise a warning if no documents are found for a single path
                logger.warn(f"No documents found for path {document}")
            total_matching_documents += current_matching_documents

        if total_matching_documents == 0:
            # but raise an error if no documents are found for all paths
            raise DolmaConfigError(f"No documents found for paths {documents}.")

        print_config(parsed_config)
        create_and_run_tagger(
            documents=documents,
            destination=parsed_config.destination,
            metadata=metadata,
            taggers=taggers,
            num_processes=parsed_config.processes,
            experiment=parsed_config.experiment,
            debug=parsed_config.debug,
        )