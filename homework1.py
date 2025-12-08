

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def create_contact(self, name, phone, email, address):
        if name in self.contacts:
            print(f"Contact '{name}' already exists!")
            return
        
        self.contacts[name] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        print(f"Contact '{name}' added successfully!")

    

    
    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)


manager = ContactManager()
manager.create_contact("Alice Smith", "555-1234", "alice@email.com", "12 Apple St")
manager.create_contact("Bob Jones", "555-5678", "bob@email.com", "34 Berry Rd")

print("\n--- All Contacts ---")
manager.list_contacts()






import uuid

class ContactDatabase:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, street, city, state, zipcode):
        contact_id = str(uuid.uuid4())
        
        self.contacts[contact_id] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": {
                "street": street,
                "city": city,
                "state": state,
                "zip": zipcode
            }
        }
        print(f"Contact '{name}' added with ID {contact_id}")
        return contact_id

    
    

    def list_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for cid, contact in self.contacts.items():
                print(f"ID: {cid}")
                print(f"  Name: {contact['name']}")
                print(f"  Phone: {contact['phone']}")
                print(f"  Email: {contact['email']}")
                print(f"  Address: {contact['address']['street']}, "
                      f"{contact['address']['city']}, "
                      f"{contact['address']['state']} "
                      f"{contact['address']['zip']}")
                print("-" * 40)


db = ContactDatabase()

alice_id = db.add_contact(
    "Alice Smith", "555-1234", "alice@email.com",
    "12 Apple St", "Springfield", "NY", "10001"
)
bob_id = db.add_contact(
    "Bob Jones", "555-5678", "bob@email.com",
    "34 Berry Rd", "Boston", "MA", "02118"
)

print("\n--- All Contacts ---")
db.list_contacts()



import uuid
import re

class ContactDatabase:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, street, city, state, zipcode):
        cid = str(uuid.uuid4())
        self.contacts[cid] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": {
                "street": street,
                "city": city,
                "state": state,
                "zip": zipcode
            }
        }
        return cid

    def get_contact(self, contact_id):
        return self.contacts.get(contact_id)

    def update_contact(self, contact_id, field, new_value):
        if contact_id not in self.contacts:
            return False
        c = self.contacts[contact_id]
        if field in {"name", "phone", "email"}:
            c[field] = new_value
            return True
        if field in {"street", "city", "state", "zip"}:
            c["address"][field] = new_value
            return True
        return False

    def delete_contact(self, contact_id):
        return self.contacts.pop(contact_id, None) is not None

    def list_contacts(self):
        return self.contacts.items()

    def _norm(self, x):
        return "" if x is None else str(x).strip().lower()

    def _get_field_value(self, c, field):
        if field in {"street","city","state","zip"}:
            return self._norm(c["address"].get(field))
        return self._norm(c.get(field))

    def search_any(self, text):
        text = self._norm(text)
        fields = ["name","phone","email","street","city","state","zip"]
        return [
            (cid,c) for cid,c in self.contacts.items()
            if any(text in self._get_field_value(c,f) for f in fields)
        ]

    def pretty(self, results):
        if not results:
            print("No results found.")
        for cid, c in results:
            addr = c["address"]
            print(f"ID: {cid}")
            print(f"  Name:   {c['name']}")
            print(f"  Phone:  {c['phone']}")
            print(f"  Email:  {c['email']}")
            print(f"  Address:{addr['street']}, {addr['city']}, {addr['state']} {addr['zip']}")
            print("-"*44)


def main():
    db = ContactDatabase()

    while True:
        print("\n Contact Manager")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            street = input("Street: ")
            city = input("City: ")
            state = input("State: ")
            zipcode = input("Zip: ")
            cid = db.add_contact(name, phone, email, street, city, state, zipcode)
            print(f" Contact added with ID: {cid}")

        elif choice == "2":
            print("\n--- All Contacts ---")
            db.pretty(db.list_contacts())

        elif choice == "3":
            text = input("Enter search text: ")
            results = db.search_any(text)
            db.pretty(results)

        elif choice == "4":
            cid = input("Enter contact ID to update: ").strip()
            field = input("Field (name, phone, email, street, city, state, zip): ").strip().lower()
            new_val = input("New value: ")
            if db.update_contact(cid, field, new_val):
                print(" Contact updated.")
            else:
                print("Update failed (invalid ID or field).")

        elif choice == "5":
            cid = input("Enter contact ID to delete: ").strip()
            if db.delete_contact(cid):
                print(" Contact deleted.")
            else:
                print(" Contact not found.")

        elif choice == "6":
            print(" Exiting Contact Manager. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

