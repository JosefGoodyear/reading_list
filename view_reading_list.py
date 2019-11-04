def view_reading_list(reading_list_file):
    """ Print your reading list to the terminal """
    try:
        with open(reading_list_file) as f:
            reading_list = f.read()
        print()
        print(reading_list)
    except IOError:
        print('{} could not be found.'.format(reading_list_file))
