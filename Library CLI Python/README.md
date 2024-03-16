# Library-CLI
Welcome to Library CLI.

This application utilizes a command line interface to work with ebooks and files. Though such a task is very difficult
through a CLI, the true purpose of this application is practice for its author to use SQL and SQLite3 in python in
preparation of using the algorithms built here for a GUI application which has the same purpose.

The following application has relatively very few commands but each command has its own share of arguments.
The commands are:
- `add`
- `del`
- `getid`
- `open`
- `reset`
- `search`
- `update`

These commands look or sound similar to SQL commands and that is because they are intentionally designed that way.

The application connects to a database "ebooks.db" or creates one if it does not exist and creates a table called
ebooks.

There are 5 fields:
- Name
- Author
- Path
- Genre
- Folder

You can work with the values of these fields using the commands above.

Note: no parameters but "specified value" means that there will be `input()` following.