class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for index, contact in enumerate(self.contacts):
                print(f"{index + 1}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts found.")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        if found_contacts:
            print("Search Results:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No matching contacts found.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                contact.phone_number = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter name of contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
