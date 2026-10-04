"""
EXERCISE 5.4: Persistent Contact Book (BONUS)

OBJECTIVE:
Create a complete contact book application that saves data to files.
Choose CSV or JSON for storage.

REQUIREMENTS:
1. Implement these functions:
   - load_contacts(filename) - Load from file
   - save_contacts(filename, contacts) - Save to file
   - add_contact(contacts, name, phone, email)
   - remove_contact(contacts, name)
   - search_contact(contacts, name)
   - list_all_contacts(contacts)
   - export_to_format(contacts, format) - Export to CSV or JSON

2. Data persistence - changes are saved to file
3. Handle file errors gracefully
4. Support both CSV and JSON formats

EXAMPLE USAGE:
contacts = load_contacts("contacts.json")
add_contact(contacts, "Alice", "555-1234", "alice@email.com")
add_contact(contacts, "Bob", "555-5678", "bob@email.com")
save_contacts("contacts.json", contacts)

# Restart program
contacts = load_contacts("contacts.json")
list_all_contacts(contacts)  # Alice and Bob are still there!

search_contact(contacts, "Alice")
remove_contact(contacts, "Bob")
save_contacts("contacts.json", contacts)

export_to_format(contacts, "csv")  # Also save as CSV

BONUS:
Add categories/tags for contacts and a search_by_tag function.

GOOD LUCK! 📇
"""

# WRITE YOUR CODE BELOW:
