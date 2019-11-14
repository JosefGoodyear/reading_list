#!/usr/bin/env python3
import unittest
import os
import io
from unittest import mock
from read import get_api_items, validate_book_choice
from book import Book
from reading_list import ReadingList


class GetApiItemsTest(unittest.TestCase):

    def test_return_length(self):
        """ Check that return length is 5 """
        items = get_api_items('test')
        self.assertEqual(len(items), 5)

    def test_empty_string_search(self):
        """ Check that user is prompted again on an empty query """
        with mock.patch('builtins.input', return_value='test'):
            items = get_api_items('')
        self.assertGreaterEqual(len(items), 0)

    def test_spaces_string_search(self):
        """ Check that user is prompted again on a query with spaces only """
        with mock.patch('builtins.input', return_value='test'):
            items = get_api_items('         ')
        self.assertGreaterEqual(len(items), 0)

    def test_no_results(self):
        """ Check that a call that yields no results returns false """
        self.assertFalse(get_api_items('kf4ierae132roiujmlero2jlk'))


class ValidateBookChoiceTest(unittest.TestCase):

    def test_nondigit_input(self):
        """ Check that non-digit input returns False """
        with mock.patch('builtins.input', return_value='a'):
            self.assertFalse(validate_book_choice([1, 2, 3, 4, 5]))

    def test_out_of_range_input(self):
        """ Check that out of range input returns False """
        with mock.patch('builtins.input', return_value='6'):
            self.assertFalse(validate_book_choice([1, 2, 3, 4, 5]))


class BookTest(unittest.TestCase):

    def setUp(self):
        """ Create a Book object """
        info = {'title': 'Fake Book', 'authors': ['Fake Author'],
                'publisher': 'Fake Publisher', 'publishedDate': '2007'}
        self.book = Book(info, 1)

    def test_init(self):
        """ Check constructor for Book class """
        self.assertEqual(self.book.id, 1)
        self.assertEqual(self.book.title, 'Fake Book')
        self.assertEqual(self.book.authors, ['Fake Author'])
        self.assertEqual(self.book.publisher, 'Fake Publisher')

    def test_convert_authors_none(self):
        """ Check that convert_authors returns None if input is None """
        self.book.authors = None
        self.assertEqual(self.book.convert_authors(), None)

    def test_convert_authors_multiple(self):
        """ Check that convert_authors returns a comma separated string """
        self.book.authors = ['Author1, Author2']
        self.assertEqual(self.book.convert_authors(), 'Author1, Author2')

    def test_str(self):
        """ Check the string representation of a Book object """
        self.assertEqual(str(self.book),
                         'Fake Book by Fake Author (Fake Publisher)')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        """ Assert stdout for print_book """
        self.book.print_book()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_book(self):
        """ Check print_book """
        self.assert_stdout(2, '\n1: Fake Book by Fake Author ' +
                              '(Fake Publisher)\n')


class ReadingListTest(unittest.TestCase):

    def setUp(self):
        """ Create a Book and ReadingList object """
        info = {'title': 'Fake Book', 'authors': ['Fake Author'],
                'publisher': 'Fake Publisher', 'publishedDate': '2007'}
        self.book = Book(info, 1)
        self.reading_list = ReadingList('TestReadingList.txt')

    def tearDown(self):
        """ If a reading list file has been created, remove it """
        if os.path.exists('TestReadingList.txt'):
            os.remove('TestReadingList.txt')

    def test_init(self):
        """ Check constructor for ReadingList class """
        self.assertEqual(self.reading_list.filename, 'TestReadingList.txt')

    def test_add_book(self):
        """ Check the add_book method """

        def find_file_length(f):
            """ Determine file length by line """
            print(len(f))
            with open(f) as f:
                for i, line in enumerate(f):
                    pass
            return i + 1

        self.reading_list.add_book(self.book)
        length_1 = find_file_length(self.reading_list.filename)
        self.reading_list.add_book(self.book)
        length_2 = find_file_length(self.reading_list.filename)
        self.assertEqual(length_1 + 1, length_2)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_add(self, n, expected_output, mock_stdout):
        """ Assert stdout for add_book failure """
        self.reading_list.filename = '/path/to/file.txt'
        self.reading_list.add_book(self.book)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_add_book_fail_to_write(self):
        """ Check message for add_book failure """
        self.assert_stdout_add(2, ('There was an error opening/writing ' +
                                   'to the file. Fake Book by Fake Author ' +
                                   '(Fake Publisher) was not added to your ' +
                                   'reading list.\n\n'))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_view(self, n, expected_output, mock_stdout):
        """ Assert stdout for view failure """
        self.reading_list.filename = 'doesNotExist.txt'
        self.reading_list.view()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_view_fail(self):
        """ Check message for view failure """
        self.assert_stdout_view(2, 'doesNotExist.txt could not be found.\n\n')


if __name__ == '__main__':
    unittest.main()
