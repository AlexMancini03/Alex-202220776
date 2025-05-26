# Function to calculate area
def calculate_area(length, width):
    return length * width

# Get user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and print area
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
