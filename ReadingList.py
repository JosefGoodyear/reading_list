from Book import Book


class ReadingList:

    def __init__(self, filename):
        self.filename = filename

    def add_book(self, book):
        """ Add a book to the reading list """
        if type(book) is not Book:
            exit()
        try:
            book = str(book)
            with open(self.filename, "a+") as f:
                f.write(book + '\n')
            print("{} was added to your reading list.".format(book))
        except IOError:
            print('There was an error opening/writing to the file.' +
                  ' {} was not added to your reading list.'.format(book))

    def view(self):
        """ View the reading list """
        try:
            with open(self.filename) as f:
                reading_list = f.read()
            print()
            print(reading_list)
        except IOError:
            print('{} could not be found.'.format(self.filename))
