"""
EXERCISE 4.4: Set Operations - Common Interests - SOLUTION
"""

def add_person(interests, name, hobbies):
    """Add a person with their hobbies (as a set)."""
    interests[name] = set(hobbies)
    print(f"Added {name} with {len(hobbies)} hobbies")

def find_common_interests(interests, person1, person2):
    """Find interests shared by two people."""
    if person1 in interests and person2 in interests:
        return interests[person1] & interests[person2]
    return set()

def find_all_interests(interests):
    """Find all unique interests across all people."""
    all_interests = set()
    for hobbies in interests.values():
        all_interests |= hobbies
    return all_interests

def find_unique_interests(interests, person):
    """Find interests that only this person has."""
    if person not in interests:
        return set()
    
    # Get this person's interests
    person_interests = interests[person]
    
    # Get all other people's interests
    others_interests = set()
    for name, hobbies in interests.items():
        if name != person:
            others_interests |= hobbies
    
    # Return interests unique to this person
    return person_interests - others_interests

def find_similar_people(interests, person, min_common=2):
    """Find people who share at least min_common interests."""
    if person not in interests:
        return []
    
    similar = []
    for name in interests:
        if name != person:
            common = find_common_interests(interests, person, name)
            if len(common) >= min_common:
                similar.append(name)
    
    return similar

def recommend_hobbies(interests, person):
    """BONUS: Recommend new hobbies based on similar people's interests."""
    if person not in interests:
        return set()
    
    # Find all similar people
    similar_people = find_similar_people(interests, person, min_common=1)
    
    # Get their interests
    recommendations = set()
    for similar_person in similar_people:
        recommendations |= interests[similar_person]
    
    # Remove hobbies the person already has
    recommendations -= interests[person]
    
    return recommendations


# Test the functions
print("=== Interest Matching System ===\n")

interests = {}

# Add people with their hobbies
add_person(interests, "Alice", {"reading", "hiking", "coding", "photography"})
add_person(interests, "Bob", {"coding", "gaming", "hiking", "music"})
add_person(interests, "Charlie", {"reading", "gaming", "music", "cooking"})
add_person(interests, "Diana", {"hiking", "photography", "travel", "reading"})
print()

# Display all people and their interests
print("=== People and Their Interests ===")
for name, hobbies in interests.items():
    print(f"{name}: {hobbies}")
print()

# Find common interests
print("=== Common Interests ===")
common = find_common_interests(interests, "Alice", "Bob")
print(f"Alice and Bob share: {common}")

common = find_common_interests(interests, "Alice", "Diana")
print(f"Alice and Diana share: {common}")

common = find_common_interests(interests, "Bob", "Charlie")
print(f"Bob and Charlie share: {common}")
print()

# Find all unique interests
all_interests = find_all_interests(interests)
print(f"All interests in the group: {all_interests}")
print(f"Total unique interests: {len(all_interests)}")
print()

# Find unique interests for each person
print("=== Unique Interests ===")
for name in interests:
    unique = find_unique_interests(interests, name)
    if unique:
        print(f"{name}'s unique interests: {unique}")
    else:
        print(f"{name} has no unique interests")
print()

# Find similar people
print("=== Similar People ===")
for name in interests:
    similar = find_similar_people(interests, name, min_common=2)
    if similar:
        print(f"People similar to {name}: {similar}")
print()

# BONUS: Hobby recommendations
print("=== BONUS: Hobby Recommendations ===")
for name in interests:
    recommendations = recommend_hobbies(interests, name)
    if recommendations:
        print(f"Recommended for {name}: {recommendations}")
    else:
        print(f"No new recommendations for {name}")
