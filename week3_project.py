import re

def add_contact(contacts):
    while True:
        identifier = input("Enter unique identifier (phone: XXX-XXX-XXXX): ")
        pattern = r"^\d{3}-\d{3}-\d{4}$"
        if not re.match(pattern, identifier):
            print("ERROR. Invalid phone format. Please enter valid phone number..")
            continue
        elif identifier in contacts:
            print("Contact with this identifier already exists.")
            return
        break
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional identifier (e.g., address, notes): ")

    if not re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
        print("Invalid phone number format. Use XXX-XXX-XXXX.")
        return
    
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Invalid email format.")
        return

    contacts[identifier] = {
        "name": name,
        "phone": phone,
        "email": email,
        "additional_info": additional_info
    }
    print("Contact added successfully.")
    


def edit_contact(contacts):
    identifier = input("Enter the unique identifier of the contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return

    print(f"Editing contact: {contacts[identifier]}")
    name = input("Enter new name (leave blank to keep current): ")
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email address (leave blank to keep current): ")
    additional_info = input("Enter new additional identifier (leave blank to keep current): ")

    if name:
        contacts[identifier]["name"] = name
    if phone:
        contacts[identifier]["phone"] = phone
    if email:
        contacts[identifier]["email"] = email
    if additional_info:
        contacts[identifier]["additional_info"] = additional_info

    print("Contact updated successfully.")


def delete_contact(contacts):
    identifier = input("Enter the unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact(contacts):
    identifier = input("Enter the unique identifier of the contact to search for: ")
    if identifier in contacts:
        print("Contact found:")
        print(contacts[identifier])
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for identifier, details in contacts.items():
            print(f"\nIdentifier: {identifier}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")


def export_contacts(contacts):
    filename = input("Enter the filename to export contacts to: ")
    try:
        with open(filename, 'w') as file:
            for identifier, details in contacts.items():
                file.write(f"Identifier: {identifier}\n")
                for key, value in details.items():
                    file.write(f"{key.capitalize()}: {value}\n")
                file.write("\n")
        print(f"Contacts exported successfully to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def import_contacts(contacts):
    filename = input("Enter the filename to import contacts from: ")
    try:
        with open(filename, 'r') as file:
            current_contact = {}
            identifier = None
            for line in file:
                line = line.strip()
                if line.startswith("Identifier:"):
                    if identifier:
                        contacts[identifier] = current_contact
                    identifier = line.split(": ")[1]
                    current_contact = {}
                elif line:
                    key, value = line.split(": ", 1)
                    current_contact[key.lower()] = value
            if identifier:
                contacts[identifier] = current_contact
        print(f"Contacts imported successfully from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def display_menu():
    print("\nWelcome to the Contact Management System")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts)
        elif choice == '7':
            import_contacts(contacts)
        elif choice == '8':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
