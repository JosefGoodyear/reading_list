class ReadingList:

    def __init__(self, filename):
        """ Initialize a ReadingList object """
        self.filename = filename

    def add_book(self, book):
        """ Add a book to the reading list """
        try:
            book = str(book)
            with open(self.filename, "a+") as f:
                f.write(book + '\n')
            print("\n{} was added to your reading list.\n".format(book))
        except IOError:
            print('There was an error opening/writing to the file.' +
                  ' {} was not added to your reading list.\n'.format(book))

    def view(self):
        """ View the reading list """
        try:
            with open(self.filename) as f:
                reading_list = f.read()
            print("\nReading List:\n")
            print(reading_list)
        except IOError:
            print('{} could not be found.\n'.format(self.filename))
