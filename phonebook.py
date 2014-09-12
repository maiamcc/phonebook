# A mini phonebook Python app based off the coding exercise written
    # by Amy Hanlon (HS W '14)

import cPickle
import os
import sys


class ArgumentError(Exception): pass


class NoFileError(Exception): pass


class NoEntryError(Exception): pass


class DuplicateError(Exception): pass


def create(phonebook_name):
    """Creates a new phonebook of the given name. (If given name
        is not a .pb file, adds '.pb'.)"""

    if phonebook_name[:-3] != ".pb":
        phonebook_name = "%s.pb" % phonebook_name

    if os.path.exists(filename):
        raise DuplicateError("That phonebook already exists!")
    else:
        with open(filename, "w") as infile:
            pass


def add(name, number, phonebook):
    """Adds new entry to specified phonebook."""

    phonebook_data = read_phonebook(phonebook)

    if phonebook_data.get(name):
        raise DuplicateError("This entry already exists. To make changes, "
                             "use update_number or update_name.")

    else:
        phonebook_data[name] = number
        print "Entry added:", name, number
        save(phonebook_data, phonebook)


def update_number(name, number, phonebook):
    """Updates an entry of given name with new number. Exact
        name matches only."""

    phonebook_data = read_phonebook(phonebook)

    if not phonebook_data.get(name):
        raise NoEntryError("This entry does not exist! "
                           "(Names are case-sensitive.)")

    else:
        print "Previous entry:", name, phonebook_data[name]
        phonebook_data[name] = number
        print "New entry:", name, phonebook_data[name]
        save(phonebook_data, phonebook)


def update_name(old_name, new_name, phonebook):
    """Updates an entry of given name with new name. Exact
        name matches only."""

    phonebook_data = read_phonebook(phonebook)

    if not phonebook_data.get(old_name):
        raise NoEntryError("This entry does not exist! "
                           "(Names are case-sensitive.)")

    else:
        print "Previous entry:", old_name, phonebook_data[old_name]
        number = phonebook_data[old_name]
        del phonebook_data[old_name]
        phonebook_data[new_name] = number
        print "New entry:", new_name, phonebook_data[new_name]
        save(phonebook_data, phonebook)


def delete(name, phonebook):
    """Deletes the entry of given name. Exact name matches only."""

    phonebook_data = read_phonebook(phonebook)

    if not phonebook_data.get(name):
        raise NoEntryError("This entry does not exist! "
                           "(Names are case-sensitive.)")

    else:
        print "Deleting entry:", name, phonebook_data[name]
        del phonebook_data[name]
        save(phonebook_data, phonebook)


def lookup(name, phonebook):
    """Given name, returns any matching entries."""

    phonebook_data = read_phonebook(phonebook)

    match = False
    for entry_name in phonebook_data:
        if name.lower() in entry_name.lower():
            match = True
            print entry_name, phonebook_data[entry_name]

    if not match:
        print "No matches found."


def reverse_lookup(number, phonebook):
    """Given number, returns all matching entries."""

    phonebook_data = read_phonebook(phonebook)

    match = False
    for entry_name, entry_number in phonebook_data.iteritems():
        if number in entry_number:
            print entry_name, entry_number
            match = True

    if not match:
        print "No matches found."


def display(phonebook):
    """Displays the contents of given phonebook in alphabetical order."""

    phonebook_data = read_phonebook(phonebook)

    for name in sorted(phonebook_data.keys(), key=str.lower):
        print name, phonebook_data[name]


def read_phonebook(phonebook):
    """Returns the dictionary of names/numbers contained in the given
        phonebook file, or throws an error if the file does not exist."""

    try:
        with open(phonebook) as infile:
            try:
                return cPickle.load(infile)
            except EOFError:
                return {}

    except IOError:
        print "That phonebook does not exist!"


def save(data, phonebook):
    """Saves the dictionary containing phonebook data to the given
        phonebook, using cPickle."""

    with open(phonebook, "w") as outfile:
        cPickle.dump(data, outfile)


def main():
    """The main function of the program."""

    # all of the functions in the program
    functions = {"create": create,
        "add" : add,
        "update_number" : update_number,
        "update_name" : update_name,
        "delete" : delete,
        "lookup" : lookup,
        "reverse_lookup" : reverse_lookup,
        "display" : display}

    args = sys.argv[:]
    script = args.pop(0)

    try:
        command = args.pop(0)
    except IndexError:
        raise ArgumentError("Not enough arguments!")

    try:
        func = functions[command]
    except KeyError:
        raise ArgumentError("Not a valid command.")

    func(*args)


if __name__ == '__main__':
    main()
