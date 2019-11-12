import requests


def get_search_obj(query):
    while query == '' or query.isspace():
        print('You entered an empty search query.')
        query = input('What do you want to search for?\n')
    url = 'https://www.googleapis.com/books/v1/volumes?q={}'.format(query)
    try:
        obj = requests.get(url).json()
    except (requests.exceptions.Re):
        print('There was an error connecting to the Google Books API.' +
              'Please check your internet connection and try again')
        exit()
    else:
        return obj


class Book:

    def __init__(self, obj, id):
        book_info = obj.get('items')[id].get('volumeInfo')
        self.id = id + 1
        self.title = book_info.get('title')
        self.authors = book_info.get('authors')
        self.publisher = book_info.get('publisher')

    def __str__(self):
        authors = self.convert_authors()
        return '{} by {} ({})'.format(self.title, authors, self.publisher)

    def convert_authors(self):
        if self.authors is None:
            return None
        else:
            return ', '.join(self.authors)

    def print_book(self):
        print('{}: {}'.format(self.id, self))


def main():
    obj = get_search_obj('baseball')
    books = []
    
    for i in range(5):
        books.append(Book(obj, i))
        books[i].print_book()


if __name__ == '__main__':
    main()
