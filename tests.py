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


class BookTest(unittest.TestCase):

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
        self.assert_stdout(2, '\n1: Fake Book by Fake Author (Fake Publisher)\n')


"""
class printBooksTest(unittest.TestCase):

    books = ["1: Python by Joseph Eddy Fontenrose (Biblo & Tannen Publishers)",
             "2: Python for Kids by Jason R. Briggs (No Starch Press)",
             "3: Learning Python by Mark Lutz (O'Reilly Media, Inc.)",
             "4: Python by Chris Fehily (Peachpit Press)",
             "5: Python for Everybody by Charles R. Severance (None)"]

    def test_out_of_range_book(self):
        with self.assertRaises(SystemExit):
            with mock.patch('builtins.input', return_value='0'):
                add_book.print_books(self.books)

    def test_book_on_edge(self):
        expected = "5: Python for Everybody by Charles R. Severance (None)"
        with mock.patch('builtins.input', return_value='5'):
            book = add_book.print_books(self.books)
            self.assertEqual(book, expected)

    def test_other_key(self):

        with self.assertRaises(SystemExit):
            with mock.patch('builtins.input', return_value='quit'):
                add_book.print_books(self.books)


class addBookToReadingListTest(unittest.TestCase):

    book1 = "2: Python for Kids by Jason R. Briggs (No Starch Press)"
    book2 = "4: Python by Chris Fehily (Peachpit Press)"

    def tearDown(self):
        if os.path.exists('TestReadingList.txt'):
            os.remove('TestReadingList.txt')

    def test_new_line_for_each_entry(self):

        def find_file_length(f):
            print(len(f))
            with open(f) as f:
                for i, line in enumerate(f):
                    pass
            return i + 1

        add_book.add_to_reading_list(self.book1, "TestReadingList.txt")
        length_1 = find_file_length("TestReadingList.txt")
        add_book.add_to_reading_list(self.book2, "TestReadingList.txt")
        length_2 = find_file_length("TestReadingList.txt")
        self.assertEqual(length_1 + 1, length_2)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        add_book.add_to_reading_list(self.book1, "path/to/file.txt")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_fail_to_write(self):
        self.assert_stdout(2, ('There was an error opening/writing ' +
                               'to the file. Python for Kids by Jason R. '
                               'Briggs (No Starch Press) ' +
                               'was not added to your reading list.\n'))


class viewReadingListTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        view_reading_list('doesNotExist.txt')
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_fail_to_open(self):
        self.assert_stdout(2, ('doesNotExist.txt could not be found.\n')) """


if __name__ == '__main__':
    unittest.main()
