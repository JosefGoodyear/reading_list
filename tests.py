import unittest, read, view_reading_list, add_book

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
        books = [['Fake Book', ['Author 1', 'Author 2'], 'Publisher']]
        formatted_books = add_book.format_books(books)
        self.assertEqual(formatted_books[0], '1: Fake Book by Author 1, Author 2 (Publisher)')
    
    def test_authors_is_none(self):
        books = [['Fake Book', None, 'Publisher']]
        formatted_books = add_book.format_books(books)
        self.assertEqual(formatted_books[0], '1: Fake Book by None (Publisher)')


if __name__ == '__main__':
    unittest.main()