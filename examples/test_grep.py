import os
import unittest

from files import grep


class GrepTestCase(unittest.TestCase):
    FILE_PATH = "test_file.txt"

    @classmethod
    def setUpClass(cls):
        with open(cls.FILE_PATH, "w") as f:
            f.write("hello world\n")
            f.write("hi there\n")
            f.write("dear world, hello!\n")
            f.write("hello\n")
            f.write("bye\n")
            f.write("hellohello\n")

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.FILE_PATH)

    def test_multiple_lines_match(self):
        result = grep(self.FILE_PATH, "hello")

        self.assertIsInstance(result, list)
        self.assertEqual(4, len(result))
        self.assertListEqual([
            "hello world\n",
            "dear world, hello!\n",
            "hello\n",
            "hellohello\n",
        ], result)

    def test_no_lines_match(self):
        for search_text in ["*", "   "]:
            with self.subTest(f"Test failed for '{search_text}'"):
                result = grep(self.FILE_PATH, search_text)

                self.assertIsInstance(result, list)
                self.assertEqual(0, len(result))

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            grep("nonexistent.txt", "hello")
