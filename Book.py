
class Book:

    def __init__(self, info, id):
        self.id = id
        self.title = info.get('title')
        self.authors = info.get('authors')
        self.publisher = info.get('publisher')

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
