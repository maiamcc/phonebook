phonebook
=========

A mini phonebook Python app based off the coding exercise written by Amy Hanlon (Hacker School W '14). Built to run from command line (from project directory, type *python phonebook.py [command] [arguments]*). Phonebook entries are name + number pairs.

### Commands

`create [phonebook_name]` - creates a new phonebook of the given name. The phonebook will be stored as [phonebook_name].txt, but for all commands that ask for a phonebook name, provide it as you did here (i.e. _without_ the `.txt`).

`add [name] [number] [phonebook]` - adds a new entry to the phonebook.

`update_number [name] [new number] [phonebook]` - finds the entry of [name] (exact name matches only) and updates the number.

`update_name [old name] [new name] [phonebook]` - updates the entry of [old name] (exact name matches only) to new name provided.

`delete [name] [phonebook]` - deletes the entry of a given name (exact name matches only).

`lookup [name] [phonebook]` - given (part of) a name, returns all matching entries.

`reverse_lookup [number] [phonebook]` - given (part of) a phone number, returns all matching entries.

`display [phonebook]` - displays the contents of given phonebook in alphabetical order.
