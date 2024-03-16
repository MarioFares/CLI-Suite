# Email Sender
Welcome to Email Sender.

This is an application with a command line interface (console) designed to make sending quick emails as easy, efficient, and fast as possible. The work is done in an interactive shell so there is no GUI.

This application makes use of the Python Standard Library modules cmd, email and smtplib which are the core of this application.

The cmd module was used to build this as an interactive shell.

The email module was used in order to create an Email instance which makes it easier to specify things such as receivers, attachments, subject and body.

The smtplib is the basic protocol we use to send the email, and we use SSL encryption.

This application is packed full of commands made to make the task of sending an email very easy.

You must specify your email username and password. Note: the email must be configured to be allowed access from less secure applications.

Then you must specify a list of receivers for this email, the body, and the subject.

There you have it: a basic email.

You are able to attach as well images, documents, and HTML files to create HTML emails.

Your inputs are saved and they include:
- Username
- Password
- List of Receivers
- Port
- Server
- Body
- Subject
- Attachments
- HTML

You have the option to save these to a JSON file, and load them from a JSON file.