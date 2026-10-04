"""
EXERCISE 4.2: Contact Book - SOLUTION
"""

def add_contact(contacts, name, phone, email, address=None):
    """Add a new contact to the contact book."""
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address if address else "N/A"
    }
    print(f"Added contact: {name}")

def remove_contact(contacts, name):
    """Remove a contact from the contact book."""
    if name in contacts:
        del contacts[name]
        print(f"Removed contact: {name}")
    else:
        print(f"Contact '{name}' not found")

def search_contact(contacts, name):
    """Search for a contact by name and display their info."""
    if name in contacts:
        print(f"\nContact: {name}")
        print(f"  Phone: {contacts[name]['phone']}")
        print(f"  Email: {contacts[name]['email']}")
        print(f"  Address: {contacts[name]['address']}")
        return contacts[name]
    else:
        print(f"Contact '{name}' not found")
        return None

def display_all_contacts(contacts):
    """Display all contacts in the contact book."""
    print(f"\n=== Contact Book ({len(contacts)} contacts) ===")
    
    if not contacts:
        print("  (empty)")
        return
    
    for name, info in contacts.items():
        print(f"\n  {name}:")
        print(f"    Phone: {info['phone']}")
        print(f"    Email: {info['email']}")
        print(f"    Address: {info['address']}")

def count_contacts(contacts):
    """Return the number of contacts."""
    return len(contacts)

def search_by_field(contacts, field, value):
    """BONUS: Search contacts by any field (phone, email, address)."""
    results = []
    for name, info in contacts.items():
        if info.get(field) == value:
            results.append(name)
    return results


# Test the functions
print("=== Contact Book Manager ===\n")

contacts = {}

# Add contacts
add_contact(contacts, "Alice", "555-1234", "alice@email.com", "123 Main St")
add_contact(contacts, "Bob", "555-5678", "bob@email.com")
add_contact(contacts, "Charlie", "555-9999", "charlie@email.com", "456 Oak Ave")
print()

# Display all
display_all_contacts(contacts)

# Count
print(f"\nTotal contacts: {count_contacts(contacts)}")

# Search for specific contact
search_contact(contacts, "Alice")
search_contact(contacts, "Dave")

# Remove a contact
print()
remove_contact(contacts, "Bob")
display_all_contacts(contacts)

# BONUS: Search by field
print("\n=== BONUS: Search by Field ===")
results = search_by_field(contacts, "phone", "555-1234")
print(f"Contacts with phone 555-1234: {results}")

results = search_by_field(contacts, "email", "charlie@email.com")
print(f"Contacts with email charlie@email.com: {results}")
