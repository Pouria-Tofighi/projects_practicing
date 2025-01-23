class ContactBook:
    """
    Initialize contact book object with an empty dictionary
    """
    def __init__(self, ):
        """
        Initial contact book object with an empty dictionary
        """
        self.contacts: dict = {}

    def add_contacts(self, name: str, phone: int, email: str, address: str):
        """
        Adds a new contact to your contact book.

        :param str name: The name of the contact.
        :param str phone: The phone of the contact.
        :param str email: The email of the contact.
        :param str address: The address of the contact. 
        """

        if name not in self.contacts:
            self.contact[name] = {'Phone Number': phone, 'Email': email, 'Address': address}
        else:
            print("Contact is already exist")
    
    def view_contacts(self, ):
        """
        Display all contacts in the contact book.
        """
        for name, info in self.contacts.items():
            print("Name:", name)
            print("Phone Number:", info['Phne Number'])
            print("Email:", info['Email'])
            print("Address:", info["Address"])

    def delete_contact(self, name):
        """
        Delets a contact from the contact book.

        :param str name: The name of the contact to delete. 
        """

        if name in self.contacts:
            del self.contacts['name']
            print("Contact was deleted successfully")
        else:
            print("Contact not found")

    def edit_contact(self, name: str, phone: str = None, Email: str = None, address: str=None):
        """
        Edits an existing contact in the contact book 

        :param str name: The name of the contact to edit
        :param str email: The email of the contact to edit.
        :param str phone: The phone of the contact to edit. 
        :param str address: The new physics address of the contact.
        """

        if name in self.contacts:
            if phone:
                self.contacts[name]["Phone Number"] = phone
            if Email:
                self.contacts[name]["Email"] = Email
            if address:
                self.contacts[name]["Address"] = address
            print("Contact updated successfully")
            return 
        print("Contact Not found")

if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\n --- Contact Book Application ---")
        print("1. Adding contact: ")
        print("2. Edit Contact: ")
        print("3. View contact: ")
        print("4. Delete contact")
        print('5. Quit')
        user_choise = input("\nPlease Enter yout choice: ")

        if user_choise == '1':
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address")
            book.add_contacts(name, phone, email, address)

        elif user_choise == "2":
            name = input('\nEnter name of the contact to edit: ')
            phone = input('Enter new/updated phone number or pass Enter to keep unchanged: ')
            email = input("Enter new/update email or pass Enter to keep unchanged")
            address = input("Enter new/update address or press Enter to keep unchanged")
            book.edit_contact(name, phone or None, email or None, address or None)

        elif user_choise == '3':
            print('\nList of contacts')
            book.view_contact()

        elif user_choise == '4':
            name = input("\nEnter name of contact to delete: ")
            book.delet_contact(name)

        elif user_choise == '5':
            print("\nThank You for using contact book application. \nGOODBYE...")
            break

        else:
            print("\nInvalid choice! please try again.")


        
            
