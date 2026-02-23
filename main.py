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



def modify_contact(contact):
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


def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contact):
            print(f"{i + 1}. {contact.f_name} {contact.l_name} - {contact.phone}")


def main():
    contacts = read_file()

    while True: 
        choice = get_menu_choice

        if choice == 1:
             display_contacts(contacts)

        elif choice == 2:
            f = input("First Name: ")
            l = input("Last Name: ")
            p = input("Phone:")
            a = input("Address:")
            c = input("City:")
            z = input("Zip:")

            new_contact = contact(f,l,p,a,c,z)
            contacts.append(new_contact)
            contacts.sort(key = lambda c:(c.l_name, c.f_name))

        elif choice == 3: 
            display_contacts(contacts)
            index = int(input("Select contact "))
            if 0 <= index < len(contacts):
                modify_contact(contacts[index])
                contacts.sort(key=lambda c: (c.l_name, c.f_name))
            else:
                print("Invalid selection.")

        elif choice == 4:
            display_contacts(contacts)
            index = int(input("Select contact number to delete"))
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
