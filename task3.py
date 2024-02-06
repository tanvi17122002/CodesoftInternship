class ContactManager:
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, search_term):
        results = [(name, details) for name, details in self.contacts.items()
                   if search_term.lower() in name.lower() or search_term in details['phone']]
        return results

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        if name in self.contacts:
            contact = self.contacts[name]
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")


# Example usage:
contact_manager = ContactManager()

# Adding contacts
contact_manager.add_contact('John Doe', '123-456-7890', 'john@example.com', '123 Main St')
contact_manager.add_contact('Jane Smith', '987-654-3210', 'jane@example.com', '456 Oak St')

# Viewing contact list
print("Contact List:")
contact_manager.view_contact_list()

# Searching for contacts
search_results = contact_manager.search_contact('John')
print("\nSearch Results:")
for name, details in search_results:
    print(f"Name: {name}, Phone: {details['phone']}")

# Updating a contact
contact_manager.update_contact('John Doe', new_phone='555-555-5555')
print("\nUpdated Contact List:")
contact_manager.view_contact_list()

# Deleting a contact
contact_manager.delete_contact('Jane Smith')
print("\nUpdated Contact List after Deletion:")
contact_manager.view_contact_list()