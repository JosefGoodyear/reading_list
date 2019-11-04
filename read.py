#!/usr/bin/env python3

from add_book import add_book
from view_reading_list import view_reading_list


def main():
    choice = input("Welcome to your reading list. Please choose an option:\n" +
                   "1: Add a book\n2: View your reading list\n3: Exit\n")
    if choice == '1':
        add_book()
    elif choice == '2':
        view_reading_list("ReadingList.txt")
    elif choice == '3':
        exit()
    else:
        print("That is not a valid choice. Please choose 1, 2, or 3.")
        main()


if __name__ == '__main__':
    main()
