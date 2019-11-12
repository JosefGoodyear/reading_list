from Book import Book


class ReadingList:

    def __init__(self, filename):
        self.filename = filename

    def add_book(self, book):
        if type(book) is not Book:
            exit()
        pass

    def view(self):
        try:
            with open(self.filename) as f:
                reading_list = f.read()
            print()
            print(reading_list)
        except IOError:
            print('{} could not be found.'.format(self.filename))


def main():
    reading_list = ReadingList('ReadingList.txt')
    reading_list.view()


if __name__ == '__main__':
    main()
