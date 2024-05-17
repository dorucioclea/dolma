"""

Tests for the utils module.

@kylel, @soldni

"""

from unittest import TestCase

from dolma.core.data_types import TextSlice
from dolma.core.utils import batch_iterator, split_paragraphs, split_sentences


class TestUtils(TestCase):
    def test_make_variable_name(self):
        pass

    def test_split_paragraphs(self):
        text = "This is a paragraph.\nThis is another paragraph.\nThis is a third paragraph."
        paragraphs = split_paragraphs(text=text)
        self.assertIsInstance(paragraphs[0], TextSlice)
        self.assertEqual(len(paragraphs), 3)
        self.assertEqual(paragraphs[0].text, "This is a paragraph.\n")
        self.assertEqual(text[paragraphs[0].start : paragraphs[0].end], paragraphs[0].text)
        self.assertEqual(paragraphs[1].text, "This is another paragraph.\n")
        self.assertEqual(text[paragraphs[1].start : paragraphs[1].end], paragraphs[1].text)

        paragraphs2 = split_paragraphs(text=text, remove_empty=False)
        self.assertListEqual([p.text for p in paragraphs], [p.text for p in paragraphs2])

    def test_split_paragraphs_empty(self):
        text = ""
        paragraphs = split_paragraphs(text=text)
        self.assertEqual(len(paragraphs), 0)

    def test_split_paragraphs_with_newline_and_spaces(self):
        text = "This is a sentence. \n  \n This is another sentence.\n\n  This is a third sentence."

        paragraphs = split_paragraphs(text=text)
        self.assertEqual(len(paragraphs), 3)
        self.assertIsInstance(paragraphs[0], TextSlice)
        self.assertEqual(len(paragraphs), 3)
        self.assertEqual(paragraphs[0].text, "This is a sentence. \n")
        self.assertEqual(text[paragraphs[0].start : paragraphs[0].end], paragraphs[0].text)
        self.assertEqual(paragraphs[1].text, " This is another sentence.\n")
        self.assertEqual(text[paragraphs[1].start : paragraphs[1].end], paragraphs[1].text)

        paragraphs = split_paragraphs(text=text, remove_empty=False)
        self.assertEqual(len(paragraphs), 5)
        self.assertIsInstance(paragraphs[0], TextSlice)
        self.assertEqual(len(paragraphs), 5)
        self.assertEqual(paragraphs[0].text, "This is a sentence. \n")
        self.assertEqual(text[paragraphs[0].start : paragraphs[0].end], paragraphs[0].text)
        self.assertEqual(paragraphs[1].text, "  \n")
        self.assertEqual(text[paragraphs[1].start : paragraphs[1].end], paragraphs[1].text)
        self.assertEqual(paragraphs[2].text, " This is another sentence.\n")
        self.assertEqual(text[paragraphs[2].start : paragraphs[2].end], paragraphs[2].text)

    def test_split_sentences(self):
        text = "This is a sentence. This is another sentence. This is a third sentence."

        sentences = split_sentences(text=text)
        self.assertIsInstance(sentences[0], TextSlice)
        self.assertEqual(len(sentences), 3)
        self.assertEqual(sentences[0].text, "This is a sentence.")
        self.assertEqual(text[sentences[0].start : sentences[0].end], sentences[0].text)
        self.assertEqual(sentences[1].text, "This is another sentence.")
        self.assertEqual(text[sentences[1].start : sentences[1].end], sentences[1].text)

    def test_split_sentences_empty(self):
        text = ""
        sentences = split_sentences(text=text)
        self.assertEqual(len(sentences), 0)

    def test_split_sentences_with_newline_and_spaces(self):
        text = "This is a sentence. \n  \n This is another sentence.\n\n  This is a third sentence."

        sentences = split_sentences(text=text)
        self.assertEqual(len(sentences), 3)
        self.assertIsInstance(sentences[0], TextSlice)
        self.assertEqual(len(sentences), 3)
        self.assertEqual(sentences[0].text, "This is a sentence.")
        self.assertEqual(text[sentences[0].start : sentences[0].end], sentences[0].text)
        self.assertEqual(sentences[1].text, "This is another sentence.")
        self.assertEqual(text[sentences[1].start : sentences[1].end], sentences[1].text)


class TestBatching(TestCase):
    def test_batching(self):
        a = [1, 2, 3, 4, 5]
        b = [6, 7, 8, 9, 0]

        output = list(batch_iterator(a, b, batch_size=2))
        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], [(1, 2), (6, 7)])
        self.assertEqual(output[1], [(3, 4), (8, 9)])
        self.assertEqual(output[2], [(5,), (0,)])

    def test_single_batching(self):
        a = [1, 2, 3, 4, 5]

        output = list(batch_iterator(a, batch_size=2))

        self.assertEqual(len(output), 3)
        self.assertEqual(output[0], [(1, 2)])
        self.assertEqual(output[1], [(3, 4)])
        self.assertEqual(output[2], [(5,)])

    def test_longer_batch_than_slice(self):
        a = list(range(3))
        b = list(range(3, 6))
        c = list(range(6, 9))

        output = list(batch_iterator(a, b, c, batch_size=4))

        self.assertEqual(len(output), 1)
        self.assertEqual(output[0], [(0, 1, 2), (3, 4, 5), (6, 7, 8)])

    def test_drop_last(self):
        a = [1, 2, 3, 4, 5]
        b = [6, 7, 8, 9, 0]

        output = list(batch_iterator(a, b, batch_size=2, drop_last=True))
        self.assertEqual(len(output), 2)
        self.assertEqual(output[0], [(1, 2), (6, 7)])
        self.assertEqual(output[1], [(3, 4), (8, 9)])
