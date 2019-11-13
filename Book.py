
class Book:

    def __init__(self, obj, id):
        book_info = obj[id].get('volumeInfo')
        self.id = id + 1
        self.title = book_info.get('title')
        self.authors = book_info.get('authors')
        self.publisher = book_info.get('publisher')

    def __str__(self):
        """ Return a formatted string of the book """
        authors = self.convert_authors()
        return '{} by {} ({})'.format(self.title, authors, self.publisher)

    def convert_authors(self):
        """ Convert authors array into a comma separated string """
        if self.authors is None:
            return None
        else:
            return ', '.join(self.authors)

    def print_book(self):
        """ Add the id of the book """
        print('\n{}: {}'.format(self.id, self))
