"""
Example 06: Dictionary Methods

Demonstrates common dictionary methods and operations.
"""

print("=== Dictionary Methods ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(f"Dictionary: {person}")
print()

print("=== Getting Keys, Values, Items ===")
keys = person.keys()
values = person.values()
items = person.items()

print(f"Keys: {list(keys)}")
print(f"Values: {list(values)}")
print(f"Items: {list(items)}")
print()

print("=== Iterating Over Dictionary ===")
# Iterate over keys
print("Keys:")
for key in person:
    print(f"  {key}")

# Iterate over values
print("\nValues:")
for value in person.values():
    print(f"  {value}")

# Iterate over key-value pairs
print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")
print()

print("=== Update Method ===")
person.update({"age": 26, "job": "Engineer"})
print(f"After update: {person}")

# Merge two dictionaries
extra_info = {"email": "alice@email.com", "phone": "555-1234"}
person.update(extra_info)
print(f"After merging: {person}")
print()

print("=== Copy Dictionary ===")
person_copy = person.copy()
person_copy["name"] = "Bob"
print(f"Original: {person['name']}")
print(f"Copy: {person_copy['name']}")
print()

print("=== Clear Dictionary ===")
temp = {"a": 1, "b": 2}
print(f"Before clear: {temp}")
temp.clear()
print(f"After clear: {temp}")
print()

print("=== Practical Example: Word Counter ===")
text = "hello world hello python world"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"Text: {text}")
print(f"Word count: {word_count}")

# Using get() method (cleaner)
word_count2 = {}
for word in words:
    word_count2[word] = word_count2.get(word, 0) + 1

print(f"Word count (using get): {word_count2}")
