#part 1
def remove_duplicates(numbers):
    return list(set(numbers))

print(remove_duplicates([1, 2, 2, 3, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]

#part 2
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)              # {1, 2, 3, 4, 5, 6}
print("Intersection:", a & b)        # {3, 4}
print("Difference (a - b):", a - b)  # {1, 2}
print("Symmetric Difference:", a ^ b) # {1, 2, 5, 6}

#part 3
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}

num = int(input("Enter a number: "))
if num in prime_numbers:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#part 4
def word_count(sentence):
    words = sentence.split()
    return {word: words.count(word) for word in words}

print(word_count("the rabbit and the hare"))  # Output: {'the': 2, 'rabbit': 1, 'and': 1, 'hare': 1}


#part 5: Student Grades
grades = {
    "Alex": [85, 90, 78],
    "Michael": [88, 76, 92]
}

# new student
grades["Michael"] = [90, 85, 88]

# Update a student's grades
grades["Alex"].append(95)

# Calculate and print average grade for each student
for student, marks in grades.items():
    avg = sum(marks) / len(marks)
    print(f"{student}: Average Grade = {avg:.2f}")


#part 6: reverse a Dictionary
def invert_dict(d):
    return {v: k for k, v in d.items()}

print(invert_dict({'a': 1, 'b': 2}))  # Output: {1: 'a', 2: 'b'}


#part 7: character frequency
def char_frequency(string):
    string = string.replace(" ", "")
    return {char: string.count(char) for char in string}

print(char_frequency("hello world"))  # Output: {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd':1}


#part 8: set from dictionary keys
sample_dict = {"name": "Alex", "age": 21, "city": "New York"}
keys_set = set(sample_dict.keys())

# Check if a specific key exists
key_to_check = "age"
print(f"'{key_to_check}' exists in set:", key_to_check in keys_set)
