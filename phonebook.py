# A mini phonebook Python app based off the coding exercise written
    # by Amy Hanlon (HS W '14)

import os
import cPickle

class ArgumentError(Exception): pass

class NoFileError(Exception): pass

class DuplicateError(Exception): pass

def create(phonebook_name):
    """Creates a new phonebook of the given name (as .txt file)."""
    filename = phonebook_name + ".txt"

    if os.path.exists(filename):
        raise DuplicateError("That phonebook already exists!")
    else:
        with open(filename, "w") as infile:
            pass

def add(name, number, phonebook):
    """Adds new entry to specified phonebook."""
    phonebook_exists(phonebook)
    pass

def update(name, number, phonebook):
    """Updates an entry of given name with new number."""
    pass

def lookup(name, phonebook):
    """Given name, returns any matching entries."""
    pass

def reverse_lookup(number):
    """Given phone number, returns corresponding entry."""
    pass

def check_num_format(number):
    """Checks if a phone number is the right length/format."""
    pass

def phonebook_exists(phonebook):
    """Throws an error if the given phonebook does not exist."""
    filename = phonebook + ".txt"
    if not os.path.exists(filename):
        raise NoFileError("That phonebook doesn not exist!")

def main():
    """The main function of the program."""
    pass

if __name__ == '__main__':
    main()