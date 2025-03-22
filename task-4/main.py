from pharse_input import pharse_input as pharse
from contact_operations import *

def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = pharse(user_input)

        if command in ["close", "exit"]:
            print("Bye!")
            break
        if command == "hello":
            print("How can i help you?")
            continue
        if command == "add":
            print(add_contact(args, contacts)) 
            continue
        if command == "change":
            print(change_contact(args, contacts)) 
            continue
        if command == "phone":
            print(show_phone(args, contacts)) 
            continue
        if command == "all":
            print(show_all(contacts)) 
            continue
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


