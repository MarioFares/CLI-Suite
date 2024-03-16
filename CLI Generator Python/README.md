# CLI-Generator
A command line interpreter for building command line interpreters.

This application is built using the cmd2 module primarily and it is a command line BASH like interpreter.

This command line interface program was designed for programmers who rely heavily on using CLI applications and who would like to generate a quick interactive shell with a CLI. It is geared towards simplicity trying to make generating such applications as swift and easy as possible.

Note that this application will generate code for your CLI application using the cmd2 library or even the almost compatible Python Native cmd library which like cmd2, is very easy to use.

You will be able to generate the basic structure of the application but as for the algorithms of your commands, you must do the coding yourself in the Python file that will be generated with
code by this application.

You also have the ability to save your information in a JSON file and load information from that file later on if you need it.

You are able to use ? symbol before any command to learn more about that command, its arguments, and what it does. You may also use that symbol in the beginning to see the list of commands available to you inside this application.

Command completion is also a feature made possible by the cmd2 module along with many other features such as use of aliases and abilities to run scripts with the commands of this CLI. It is worth noting that using cmd2 also makes the application stable for any explicitly uncaught errors are caught by the
module itself.