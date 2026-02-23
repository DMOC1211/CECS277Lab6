'''
Names: Daniel Puerto & Jacob Miranda
Date: 2/23/26
Group: 12
Description:
'''

import contact
FILENAME = "addresses.txt"


def read_file():
    contacts = []
    
    try: 
        with open(FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    data = line.split(",")
                    contact = contact(
                        data[0]
                        data[1]
                        data[2]
                        data[3]
                        data[4]
                        data[5]
                    )
                    contacts.append(contact)
        contacts.sort(key=lambda c: (c.l_name, c.f_name))

    except FileNotFoundError:
        pass    
    return contacts


def write_file(contacts):
    with open(FILENAME, "w") as file:
        for contact in contacts:
            file.write(repr(contact)+"\n")


def get_menu_choice():
    print("\nContact Manager")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Modify Contact")
    print("4. Delete Contact")
    print("5. Save")
    print("6. Exit")

    while True: 
        try:
            choice = int(input("Enter choice(1-6)"))
            if 1 <= choice <= 6:
                return choice
        except ValueError:
            pass
        print("Invalid choice. Try again.")



def modify_contact(cont):
    while True:
        print("\nModify Contact")
        print("1. First Name")
        print("2. Last Name")
        print("3.Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip")
        print("7. Done")

        choice = input("Choose field to modify")

        if choice == "1":
            contact.f_name = input("New First Name:")
        elif choice == "2":
            contact.l_name = input("New Last Name:")
        elif choice == "3":
            contact.phone = input("New Phone Number:")
        elif choice == "4":
            contact.address = input("New Address:")
        elif choice == "5":
            contact.city = input("New City:")
        elif choice == "6":
            contact.zip = input("New zip:")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

    return contact


def display_contacts(contact):
    

