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


if __name__ == '__main__':
    unittest.main()