import unittest
import os
import sys
from csv import reader

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.process_file import process_file


class ProcessFileTests(unittest.TestCase):

    def test_file_creation_utf_8(self):
        """Test if process_file() will create file while given valid file in input (utf-8 input)"""
        process_file('./test_files/correct.csv', 'test_correct')

        self.assertTrue(os.path.isfile('../processed_files/test_correct.csv'))

    def test_file_creation_utf_16(self):
        """Test if process_file() will create file while given valid file in input (utf-16 input)"""
        process_file('./test_files/utf16_file.csv', 'test_correct')

        self.assertTrue(os.path.isfile('../processed_files/test_correct.csv'))

    def test_wrong_format(self):
        """Test if function will stop in case if file with wrong format (in this case != .csv) passed"""
        file = process_file('./test_files/wrong_file_format.log', 'test_correct')

        self.assertFalse(file)
        os.remove(f'{os.getcwd()}/../processed_files/test_correct.csv')     # Remove created test_correct.csv file

    def test_empty_file(self):
        """Test if process_file() will break after passing empty file"""
        file = process_file('./test_files/empty.csv', 'test_empty')

        self.assertFalse(file)


if __name__ == "__main__":
    unittest.main()