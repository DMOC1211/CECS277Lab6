'''
Names: Daniel Puerto & Jacob Miranda
Date: 2/23/26
Group: 12
Description:
'''

import check_input
from contact import Contact
FILENAME = "addresses.txt"


def read_file():
    contacts = []
    
    try: 
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(",")
                    c = Contact(
                        data[0],
                        data[1],
                        data[2],
                        data[3],
                        data[4],
                        data[5]
                    )
                    
                    contacts.append(c)
                    
        contacts.sort()

    except FileNotFoundError:
        pass    
    return contacts


def write_file(contacts):
    with open(FILENAME, "w") as file:
        for c in contacts:
            file.write(repr(c)+"\n")


def get_menu_choice():
    print("\nContact Manager")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Modify Contact")
    print("4. Delete Contact")
    print("5. Save")
    print("6. Exit")

    return choice = check_input.get_int_range("Enter choice(1-6)", 1, 6)



def modify_contact(contact):
    while True:
        print("\nModify Contact")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Done")

        choice = input("Choose field to modify")

        if choice == "1":
            contact._first_name = input("New First Name:")
        elif choice == "2":
            contact._last_name = input("New Last Name:")
        elif choice == "3":
            contact._phone_number = check_input.get_positive_int("New Phone Number:")
        elif choice == "4":
            contact._address = input("New Address:")
        elif choice == "5":
            contact._city = input("New City:")
        elif choice == "6":
            contact._zip_code = check_input.get_positive_int("New zip:")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

    return contact


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, c in enumerate(contacts):
            print(f"{i + 1}. {c._first_name} {c._last_name} - {c._phone_number}")


def main():
    contacts = read_file()

    while True: 
        choice = get_menu_choice()

        if choice == 1:
             display_contacts(contacts)

        elif choice == 2:
            f = input("First Name: ")
            l = input("Last Name: ")
            p = input("Phone:")
            a = input("Address:")
            c = input("City:")
            z = input("Zip:")

            new_contact = Contact(f, l, p, a, c, z)
            contacts.append(new_contact)
            contacts.sort()

        elif choice == 3: 
            display_contacts(contacts)
            index = check_input.get_int_range("Select contact: ", 1, len(contacts)) - 1 
            if 0 <= index < len(contacts): 
                modify_contact(contacts[index])
                contacts.sort()
            else:
                print("Invalid selection.")

        elif choice == 4:
            display_contacts(contacts)
            index = check_input.get_int_range("Select contact number to delete", 1, len(contacts)) - 1
            if 0 <= index < len(contacts):
                contacts.pop(index)
                print("Contact deleted.")
            else:
                print("Invalid Selection.")

        elif choice == 5:
            write_file(contacts)
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
