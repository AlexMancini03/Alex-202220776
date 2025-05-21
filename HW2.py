# Program to convert days into seconds and minutes

days = int(input("Enter the number of days: "))

# Convert days to minutes and seconds
minutes = days * 24 * 60
seconds = days * 24 * 60 * 60

# result
print(f"{days} days is equal to {minutes} minutes or {seconds} seconds.")