# ============================================================
# 10 - Data Structures
# Python has 4 built-in collections: List, Tuple, Dict, Set.
# Each has a different purpose — pick the right one for the job.
# ============================================================

# ============================================================
# LISTS — ordered, mutable (changeable), allows duplicates
# Use for: sequences of items that may change over time
# ============================================================
print("══ LISTS ═══════════════════════════")

fruits  = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 20, 10]

# Access by index (starts at 0)
print(fruits[0])            # → apple
print(fruits[-1])           # → cherry (last item)

# Modify
fruits[1] = "mango"
print(fruits)               # → ['apple', 'mango', 'cherry']

# Add / Remove
fruits.append("grape")      # add to end
fruits.insert(1, "kiwi")    # insert at position
fruits.pop()                # remove last
fruits.remove("kiwi")       # remove by value
print(fruits)

# Useful built-ins
print(len(fruits))                          # length
print(sorted(["banana", "apple", "mango"])) # sorted copy
print(numbers.count(10))                    # count occurrences
print(numbers.index(20))                    # find position

# Loop with index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# List comprehension — build a list in one line
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares: {squares}")               # → [1, 4, 9, 16, 25]

# Filtering with comprehension
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Evens:   {evens}")                 # → [2, 4, 6, 8, 10]


# ============================================================
# TUPLES — ordered, immutable (cannot change), allows duplicates
# Use for: fixed data like coordinates, RGB values, DB records
# ============================================================
print("\n══ TUPLES ══════════════════════════")

point   = (10, 20)
person  = ("Kavya", 25, "Chitradurga")

print(person[0])            # → Kavya  (indexing works same as list)

# Tuple unpacking — assign each element to a variable
name, age, city = person
print(f"{name} is {age} from {city}.")

# Tuples are immutable — this would raise a TypeError:
# person[0] = "Riya"


# ============================================================
# DICTIONARIES — key-value pairs, ordered (Python 3.7+), mutable
# Use for: structured data with named fields (like a form)
# ============================================================
print("\n══ DICTIONARIES ════════════════════")

student = {
    "name"   : "Dennis",
    "age"    : 25,
    "grade"  : "A",
    "courses": ["Math", "Science", "English"]
}

# Access
print(student["name"])                              # → Dennis
print(student.get("phone", "Not provided"))         # → Not provided (safe access)

# Add / Update / Delete
student["phone"] = "9876543210"     # add new key
student["age"]   = 26               # update existing key
student.pop("grade")                # remove key

# Loop over key-value pairs
print("\nStudent profile:")
for key, value in student.items():
    print(f"  {key}: {value}")


# ============================================================
# SETS — unordered, no duplicates, mutable
# Use for: removing duplicates or checking membership quickly
# ============================================================
print("\n══ SETS ════════════════════════════")

raw_scores = [95, 80, 95, 70, 80, 90, 70, 95]
unique_scores = set(raw_scores)
print(f"Raw:    {raw_scores}")
print(f"Unique: {unique_scores}")       # duplicates removed

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"Union:        {a | b}")        # all elements
print(f"Intersection: {a & b}")        # common elements
print(f"Difference:   {a - b}")        # in a but not b

# Membership check — very fast on sets
print(3 in unique_scores)              # → True


# ── Quick Comparison ─────────────────────────────────────────
print("\n── Which collection to use? ────────")
print("  List  → ordered, changeable, allows duplicates")
print("  Tuple → ordered, fixed, allows duplicates")
print("  Dict  → named keys, changeable, keys unique")
print("  Set   → unordered, changeable, no duplicates")