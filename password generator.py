import re
import random
import string

# Email validation function
def is_valid_email(email):
    # Regular expression for basic email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False

# Password generator function
def generate_password(length=12):
    # Define the characters that will be used in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Ensure the password is of the specified length
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Test the functions
email = input("Enter your email: ")
if is_valid_email(email):
    print("The email is valid.")
else:
    print("The email is invalid.")

password_length = int(input("Enter the desired password length: "))
generated_password = generate_password(password_length)
print(f"Generated password: {generated_password}")
