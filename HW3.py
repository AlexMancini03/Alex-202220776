# Initialize an empty list to store the numbers
numbers = []

# Prompt the user to enter 5 numbers
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display the original list
print("\nOriginal list:", numbers)

# Sort the list in ascending order
numbers.sort()
print("Sorted list:", numbers)

# Remove the largest number (last element in the sorted list)
largest_number = numbers.pop()
print("Updated list after removing the largest number:", numbers)

# Calculate the average of the remaining numbers
if numbers:
    average = sum(numbers) / len(numbers)
    print("Average of the remaining numbers:", average)
else:
    print("No numbers left to calculate the average.")
