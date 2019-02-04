import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.process_file import process_file


class ProcessFileTests(unittest.TestCase):

    def test_process_file(self):
        """Test if process_file() will create file while given valid file in input"""
        process_file('./test_files/correct.csv', 'test_correct')

        self.assertTrue(os.path.isfile('../processed_files/test_correct.csv'))


if __name__ == "__main__":
    unittest.main()