import re

# Sample text
text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

# Regular expression pattern for emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Extract email addresses
emails = re.findall(email_pattern, text)

# Print the extracted emails
print("Extracted Email Addresses:", emails)
