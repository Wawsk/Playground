"""
OOP Email Simulator

This application simulates a basic email system with inbox management
features. Users can create mock emails, view their inbox, mark emails
as read, and quit the application.

Classes:
    Email: Represents an email object with attributes such as email address,
    subject line, email content, and read status.
        Methods:
            __init__(): Initializes a new Email object.
            mark_as_read(): Marks the email as read.

Functions:
    populate_inbox(): Prompts the user to create mock emails and adds them
    to the inbox list.

    list_emails(only_unread=False): Lists the emails in the inbox along with
    their read status. If 'only_unread' is True, it lists only the unread emails.

    read_email(index): Displays the details of a selected email and
    marks it as read.
    
Main Program:
    The main program starts by populating the inbox with mock emails using the
    'populate_inbox()' function.
    It then presents a menu to the user with the following options:
        1. Read an email: Allows the user to select and read an email.
        2. View unread emails: Displays only the unread emails.
        3. Quit application: Exits the application.

    The user is prompted to enter a selection, and the program performs the
    corresponding action based on the user's choice.

"""
from os import system
from re import match

### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email():
    """
    Represents an email object.

    Attributes:
        email_address (str): The email address of the sender.
        subject_line (str): The subject line of the email.
        email_content (str): The content of the email.
        has_been_read (bool): Indicates whether the email has been read (True) or not (False).

    Methods:
        mark_as_read(): Marks the email as read by setting the 'has_been_read' attribute to True.
    """
    # Class variable
    has_been_read = False

    # Class constructor
    def __init__ (self, email_address, subject_line, email_content):
        """ Initialises a new Email object."""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Class method
    def mark_as_read(self):
        """ Marks the email as read by setting the 'has_been_read' attribute to True."""
        self.has_been_read = True

# --- Lists --- #
inbox = []

# --- Functions --- #
def populate_inbox():
    """ Creates 3 emails and stores them in inbox list."""
    email_format_regex = r'^.+@\w+\.\w+$'
    for _ in range(3):
        system("cls")
        print("\nWelcome to the Email app. Please create some mock emails first:\n")
        while True:
            email_address = input("Enter email address: ")
            if match(email_format_regex, email_address):
                break
            else:
                print("### Invalid email format. Please enter a valid email address. ###")
        subject_line = input("Enter email subject: ")
        email_content = input("Enter email body: ")

        # Create Email object
        new_email = Email(email_address, subject_line, email_content)

        # Add Email object to inbox list
        inbox.append(new_email)
        print("\n(Emails have been added to the inbox.)\n")

def list_emails(only_unread=False):
    """ Displays all unread emails from inbox list."""
    if only_unread:
        unread_emails = [email for email in inbox if not email.has_been_read]
        for i, email in enumerate(unread_emails):
            print(f"\n{i}. Subject: {email.subject_line} (Unread)")
    else:
        for i, email in enumerate(inbox):
            status = "Unread" if not email.has_been_read else "Read"
            print(f"\n{i}. Subject: {email.subject_line} ({status})")

def read_email(index):
    """ Displays content of a selected email from inbox list."""
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"\nBody: {email.email_content}")
        print(f"\n\n(Email from {email.email_address} marked as read.)")
        email.mark_as_read()
    else:
        print("\n### Invalid email index ###")


# --- Email Program --- #
populate_inbox()

MENU = True

while MENU:
    try:
        user_choice = int(input("""\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: """))

        if user_choice == 1:
            system("cls")
            print("_"*25)
            print("\nDisplaying all emails...")
            list_emails()
            print("_"*25)
            email_choice = int(input("\nEnter the index of the email you want to read: "))
            system("cls")
            print("_"*25)
            print("\nDisplaying selected email...")
            read_email(email_choice)
            print("_"*25)
        elif user_choice == 2:
            system("cls")
            print("_"*25)
            print("\nDisplaying unread emails...")
            list_emails(only_unread=True)
            print("_"*25)
        elif user_choice == 3:
            print("\n### Exiting application ###\n")
            break
        else:
            print("\n### Incorrect input ###\n")
    except ValueError:
        print("\n### Please enter a valid number ###\n")
