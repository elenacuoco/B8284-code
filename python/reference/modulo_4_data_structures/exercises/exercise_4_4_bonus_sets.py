"""
EXERCISE 4.4: Set Operations - Common Interests (BONUS)

OBJECTIVE:
Use sets to find common interests between friends.

REQUIREMENTS:
1. Create a dictionary where keys are names and values are sets of hobbies
2. Implement these functions:
   - add_person(interests, name, hobbies)
   - find_common_interests(interests, person1, person2)
   - find_all_interests(interests)
   - find_unique_interests(interests, person)
   - find_similar_people(interests, person, min_common=2)

EXAMPLE USAGE:
interests = {}
add_person(interests, "Alice", {"reading", "hiking", "coding"})
add_person(interests, "Bob", {"coding", "gaming", "hiking"})
add_person(interests, "Charlie", {"reading", "gaming", "music"})

common = find_common_interests(interests, "Alice", "Bob")
print(f"Alice and Bob share: {common}")

EXPECTED OUTPUT:
Alice and Bob share: {'coding', 'hiking'}
All interests: {'reading', 'hiking', 'coding', 'gaming', 'music'}
Alice's unique interests: {'reading'}
People similar to Alice: ['Bob']

BONUS:
Create a recommendation system that suggests hobbies based on friends' interests.

GOOD LUCK! 🎯
"""

# WRITE YOUR CODE BELOW:
