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
    """Creates a new phonebook of the given name (as .txt file)."""

    filename = phonebook_name + ".txt"

    if os.path.exists(filename):
        raise DuplicateError("That phonebook already exists!")
    else:
        with open(filename, "w") as infile:
            pass


def add(name, number, phonebook):
    """Adds new entry to specified phonebook."""

    phonebook_data = read_phonebook(phonebook)

    if phonebook_data.get(name):
        raise DuplicateError("This entry already exists. To make changes, use update_number or update_name.")
    else:
        phonebook_data[name] = number
        print "Entry added:", name, number
        save(phonebook_data, phonebook)


def update_number(name, number, phonebook):
    """Updates an entry of given name with new number. Exact
        name matches only."""

    phonebook_data = read_phonebook(phonebook)

    if not phonebook_data.get(name):
        raise NoEntryError("This entry does not exist! (Names are case-sensitive.)")
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
        raise NoEntryError("This entry does not exist! (Names are case-sensitive.)")
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
        raise NoEntryError("This entry does not exist! (Names are case-sensitive.)")
    else:
        print "Deleting entry:", name, phonebook_data[name]
        del phonebook_data[name]
        save(phonebook_data, phonebook)


def lookup(name, phonebook):
    """Given name, returns any matching entries."""

    phonebook_data = read_phonebook(phonebook)

    match = False
    for key in phonebook_data:
        if key.lower().find(name.lower()) > -1:
            match = True
            print key, phonebook_data[key]

    if not match:
        print "No matches found."


def reverse_lookup(number, phonebook):
    """Given number, returns all matching entries."""

    phonebook_data = read_phonebook(phonebook)

    match = False
    for key, value in phonebook_data.iteritems():
        if value.find(number) > -1:
            print key, value
            match = True
            break

    if not match:
        print "No matches found."


def display(phonebook):
    """Displays the contents of given phonebook in alphabetical order."""

    phonebook_data = read_phonebook(phonebook)

    for key in sorted(phonebook_data.keys(), key=str.lower):
        print key, phonebook_data[key]


def read_phonebook(phonebook):
    """Returns the dictionary of names/numbers contained in the given
        phonebook file, or throws an error if the file does not exist."""

    filename = phonebook + ".txt"
    if not os.path.exists(filename):
        raise NoFileError("That phonebook doesn not exist!")
    else:
        with open(filename) as infile:
            if infile.read(1):
                infile.seek(0)
                return cPickle.load(infile)
            else:
                return {}


def save(data, phonebook):
    """Saves the dictionary containing phonebook data to the given
        phonebook, using cPickle."""

    filename = phonebook + ".txt"

    with open(filename, "w") as outfile:
        cPickle.dump(data, outfile)


def main():
    """The main function of the program."""

    # all of the functions in the program, and the arguments that they require
    functions = {"create": [create, ["phonebook"]],
        "add": [add, ["name", "number", "phonebook"]],
        "update_number": [update_number, ["name", "new number", "phonebook"]],
        "update_name": [update_name, ["old name", "new name", "phonebook"]],
        "delete": [delete, ["name", "phonebook"]],
        "lookup": [lookup, ["name", "phonebook"]],
        "reverse_lookup": [reverse_lookup, ["number", "phonebook"]],
        "display": [display, ["phonebook"]]}

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

    try:
        func[0](*args)
    except TypeError:
        print "Arguments required: %s." % ", ".join(func[1])


if __name__ == '__main__':
    main()
