#!/usr/bin/env python3
import unittest
import add_book
from unittest import mock


class searchTest(unittest.TestCase):

    def test_full_return_length(self):
        books = add_book.search('test')
        self.assertEqual(len(books), 5)

    def test_nested_array_length(self):
        books = add_book.search('test')
        self.assertEqual(len(books[0]), 3)

    def test_empty_return(self):
        with self.assertRaises(SystemExit):
            add_book.search('kf4ieraeroiujero2jlk')


class formatBooksTest(unittest.TestCase):

    def test_multiple_authors(self):
        expected = '1: Fake Book by Author 1, Author 2 (Publisher)'
        books = [['Fake Book', ['Author 1', 'Author 2'], 'Publisher']]
        formatted_books = add_book.format_books(books)
        self.assertEqual(formatted_books[0], expected)

    def test_authors_is_none(self):
        expected = '1: Fake Book by None (Publisher)'
        books = [['Fake Book', None, 'Publisher']]
        formatted_books = add_book.format_books(books)
        self.assertEqual(formatted_books[0], expected)


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


if __name__ == '__main__':
    unittest.main()
