import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.process_file import process_file


class ProcessFileTests(unittest.TestCase):

    def test_file_creation(self):
        """Test if process_file() will create file while given valid file in input"""
        process_file('./test_files/correct.csv', 'test_correct')

        self.assertTrue(os.path.isfile('../processed_files/test_correct.csv'))

    def test_wrong_format(self):
        """Test if function will stop in case if file with wrong format (in this case != .csv) passed"""
        file = process_file('./test_files/wrong_file_format.log', 'test_correct')

        self.assertFalse(file)

    def tearDown(self):
        """Remove test_correct.csv file after testing"""
        os.remove(f'{os.getcwd()}/../processed_files/test_correct.csv')


if __name__ == "__main__":
    unittest.main()