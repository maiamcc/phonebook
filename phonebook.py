# A mini phonebook Python app based off the coding exercise written
    # by Amy Hanlon (HS W '14)

import os
import cPickle
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
    phonebook_data = phonebook_exists(phonebook)

    if phonebook_data.get(name):
        raise DuplicateError("This entry already exists. To make \
            changes, use update_number or update_name.")
    else:
        phonebook_data[name] = number
        print "Entry added:", name, number
        save(phonebook_data, phonebook)


def update_number(name, number, phonebook):
    """Updates an entry of given name with new number. Exact
        name matches only."""
    phonebook_data = phonebook_exists(phonebook)

    if not phonebook_data.get(name):
        raise NoEntryError("This entry does not exist! (Names \
            are case-sensitive.)")
    else:
        print "Previous entry:", name, phonebook_data[name]
        phonebook_data[name] = number
        print "New entry:", name, phonebook_data[name]
        save(phonebook_data, phonebook)

def update_name(old_name, new_name, phonebook):
    """Updates an entry of given name with new name. Exact
        name matches only."""
    phonebook_data = phonebook_exists(phonebook)

    if not phonebook_data.get(old_name):
        raise NoEntryError("This entry does not exist! (Names \
            are case-sensitive.)")
    else:
        print "Previous entry:", old_name, phonebook_data[old_name]
        number = phonebook_data[old_name]
        del phonebook_data[old_name]
        phonebook_data[new_name] = number
        print "New entry:", new_name, phonebook_data[new_name]
        save(phonebook_data, phonebook)

def delete(name, phonebook):
    """Deletes the entry of given name. Exact name matches only."""

    phonebook_data = phonebook_exists(phonebook)

    if not phonebook_data.get(name):
        raise NoEntryError("This entry does not exist! (Names \
            are case-sensitive.)")
    else:
        print "Deleting entry:", name, phonebook_data[name]
        del phonebook_data[name]
        save(phonebook_data, phonebook)

def lookup(name, phonebook):
    """Given name, returns any matching entries."""

    phonebook_data = phonebook_exists(phonebook)

    match = False
    for key in phonebook_data:
        if key.lower().find(name.lower()) > -1:
            match = True
            print key, phonebook_data[key]

    if not match:
        print "No matches found."

def lookup_exact(name, phonebook):
    """Given name, returns its corresponding entry (exact matches only)."""
    phonebook_data = phonebook_exists(phonebook)

    if phonebook_data.get(name):
        print name, phonebook_data[name]
    else:
        print "No matches found."

def reverse_lookup(number, phonebook):
    """Given number, returns all matching entries."""

    phonebook_data = phonebook_exists(phonebook)

    match = False
    for key, value in phonebook_data.iteritems():
        if value.find(number) > -1:
            print key, value
            match = True
            break

    if not match:
        print "No matches found."

def phonebook_exists(phonebook):
    """Returns the dictionary of names/numbers contained in the given
        phonebook file, or throws an error if the file does not exist."""
    filename = phonebook + ".txt"
    if not os.path.exists(filename):
        raise NoFileError("That phonebook doesn not exist!")
    else:
        with open(filename) as infile:
            return cPickle.load(infile)

def save(data, phonebook):
    """Saves the dictionary containing phonebook data to the given
        phonebook, using cPickle."""
    filename = phonebook + ".txt"

    with open(filename, "w") as outfile:
        cPickle.dump(data, outfile)

def main():
    """The main function of the program."""

    args = sys.argv[:]
    script = args.pop(0)
    print "Script name:", script
    command = args.pop(0)
    print "Command name:", command

    functions = {"create": create,
        "add": add,
        "update_number": update_number,
        "update_name": update_name,
        "delete": delete,
        "lookup": lookup,
        "lookup_exact": lookup_exact,
        "reverse_lookup": reverse_lookup}

    func = functions[command]
    func(*args)

if __name__ == '__main__':
    main()