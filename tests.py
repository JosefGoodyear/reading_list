#!/usr/bin/env python3
import unittest
import os
import io
from unittest import mock
from read import get_api_items
from Book import Book
from ReadingList import ReadingList


class getApiItemsTest(unittest.TestCase):

    def test_return_length(self):
        items = get_api_items('test')
        self.assertEqual(len(items), 5)

    def test_empty_string_search(self):
        with mock.patch('builtins.input', return_value='test'):
            items = get_api_items('')
        self.assertGreaterEqual(len(items), 0)

    def test_spaces_string_search(self):
        with mock.patch('builtins.input', return_value='test'):
            items = get_api_items('         ')
        self.assertGreaterEqual(len(items), 0)

    def test_bad_search(self):
        self.assertFalse(get_api_items('kf4ierae132roiujmlero2jlk'))


class bookTest(unittest.TestCase):

    def setUp(self):
        info = {'title': 'Fake Book', 'authors': ['Fake Author'],
                'publisher': 'Fake Publisher', 'publishedDate': '2007'}
        self.book = Book(info, 1)

    def test_init(self):
        self.assertEqual(self.book.id, 1)
        self.assertEqual(self.book.title, 'Fake Book')
        self.assertEqual(self.book.authors, ['Fake Author'])
        self.assertEqual(self.book.publisher, 'Fake Publisher')

    def test_convert_authors_none(self):
        self.book.authors = None
        self.assertEqual(self.book.convert_authors(), None)

    def test_convert_authors_multiple(self):
        self.book.authors = ['Author1, Author2']
        self.assertEqual(self.book.convert_authors(), 'Author1, Author2')

    def test_str(self):
        self.assertEqual(str(self.book),
                         'Fake Book by Fake Author (Fake Publisher)')

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        self.book.print_book()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_book(self):
        self.assert_stdout(2, '\n1: Fake Book by Fake Author ' +
                              '(Fake Publisher)\n')


class readingListTest(unittest.TestCase):

    def setUp(self):
        info = {'title': 'Fake Book', 'authors': ['Fake Author'],
                'publisher': 'Fake Publisher', 'publishedDate': '2007'}
        self.book = Book(info, 1)
        self.reading_list = ReadingList('TestReadingList.txt')

    def tearDown(self):
        if os.path.exists('TestReadingList.txt'):
            os.remove('TestReadingList.txt')

    def test_init(self):
        self.assertEqual(self.reading_list.filename, 'TestReadingList.txt')

    def test_add_book(self):

        def find_file_length(f):
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
        self.reading_list.filename = '/path/to/file.txt'
        self.reading_list.add_book(self.book)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_add_book_fail_to_write(self):
        self.assert_stdout_add(2, ('There was an error opening/writing ' +
                                   'to the file. Fake Book by Fake Author ' +
                                   '(Fake Publisher) was not added to your ' +
                                   'reading list.\n\n'))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_view(self, n, expected_output, mock_stdout):
        self.reading_list.filename = 'doesNotExist.txt'
        self.reading_list.view()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_view_fail(self):
        self.assert_stdout_view(2, 'doesNotExist.txt could not be found.\n\n')


if __name__ == '__main__':
    unittest.main()
