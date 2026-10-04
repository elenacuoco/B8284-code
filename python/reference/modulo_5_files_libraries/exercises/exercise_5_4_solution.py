"""
EXERCISE 5.4: Persistent Contact Book - SOLUTION
"""

import json
import csv
import os


def load_contacts(filename):
    """Load contacts from JSON file."""
    try:
        if not os.path.exists(filename):
            print(f"File '{filename}' not found. Creating new contact list.")
            return []
        
        with open(filename, "r") as file:
            contacts = json.load(file)
        
        print(f"✓ Loaded {len(contacts)} contacts from {filename}")
        return contacts
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{filename}'")
        return []
    except Exception as e:
        print(f"Error loading contacts: {e}")
        return []


def save_contacts(filename, contacts):
    """Save contacts to JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(contacts, file, indent=2)
        print(f"✓ Saved {len(contacts)} contacts to {filename}")
        return True
    except Exception as e:
        print(f"Error saving contacts: {e}")
        return False


def add_contact(contacts, name, phone, email, tags=None):
    """Add a new contact."""
    # Check if contact already exists
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Contact '{name}' already exists")
            return False
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "tags": tags if tags else []
    }
    
    contacts.append(contact)
    print(f"✓ Added contact: {name}")
    return True


def remove_contact(contacts, name):
    """Remove a contact by name."""
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            removed = contacts.pop(i)
            print(f"✓ Removed contact: {removed['name']}")
            return True
    
    print(f"Contact '{name}' not found")
    return False


def search_contact(contacts, name):
    """Search for a contact by name."""
    for contact in contacts:
        if name.lower() in contact["name"].lower():
            print(f"\nFound: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            if contact.get("tags"):
                print(f"  Tags: {', '.join(contact['tags'])}")
            return contact
    
    print(f"Contact '{name}' not found")
    return None


def list_all_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts found")
        return
    
    print(f"\n=== Contact Book ({len(contacts)} contacts) ===")
    for contact in sorted(contacts, key=lambda c: c["name"]):
        print(f"\n{contact['name']}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
        if contact.get("tags"):
            print(f"  Tags: {', '.join(contact['tags'])}")


def export_to_csv(contacts, filename):
    """Export contacts to CSV file."""
    try:
        with open(filename, "w", newline='') as file:
            fieldnames = ["name", "phone", "email", "tags"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for contact in contacts:
                # Convert tags list to string
                contact_copy = contact.copy()
                contact_copy["tags"] = "; ".join(contact.get("tags", []))
                writer.writerow(contact_copy)
        
        print(f"✓ Exported to {filename}")
        return True
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return False


def search_by_tag(contacts, tag):
    """BONUS: Search contacts by tag."""
    results = []
    for contact in contacts:
        if tag.lower() in [t.lower() for t in contact.get("tags", [])]:
            results.append(contact)
    return results


# Test the contact book
print("=== Persistent Contact Book ===\n")

contact_file = "contacts.json"

# Load existing contacts (or create new list)
print("1. Loading contacts...")
contacts = load_contacts(contact_file)

# Add contacts
print("\n2. Adding contacts...")
add_contact(contacts, "Alice", "555-1234", "alice@email.com", ["work", "friend"])
add_contact(contacts, "Bob", "555-5678", "bob@email.com", ["family"])
add_contact(contacts, "Charlie", "555-9999", "charlie@email.com", ["work"])
add_contact(contacts, "Diana", "555-1111", "diana@email.com", ["friend", "gym"])

# Save contacts
print("\n3. Saving contacts...")
save_contacts(contact_file, contacts)

# List all contacts
list_all_contacts(contacts)

# Search for contact
print("\n4. Searching for 'Alice'...")
search_contact(contacts, "Alice")

# BONUS: Search by tag
print("\n5. Searching by tag 'work' (BONUS)...")
work_contacts = search_by_tag(contacts, "work")
print(f"Found {len(work_contacts)} contacts with tag 'work':")
for contact in work_contacts:
    print(f"  - {contact['name']}")

print("\n6. Searching by tag 'friend' (BONUS)...")
friend_contacts = search_by_tag(contacts, "friend")
print(f"Found {len(friend_contacts)} contacts with tag 'friend':")
for contact in friend_contacts:
    print(f"  - {contact['name']}")

# Remove a contact
print("\n7. Removing 'Bob'...")
remove_contact(contacts, "Bob")
save_contacts(contact_file, contacts)

# Export to CSV
print("\n8. Exporting to CSV...")
export_to_csv(contacts, "contacts.csv")

# Reload to demonstrate persistence
print("\n9. Reloading from file...")
contacts = load_contacts(contact_file)
print(f"   {len(contacts)} contacts loaded (Bob is gone!)")

list_all_contacts(contacts)

print("\n=== Contact Book System Complete! ===")
