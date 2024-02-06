import random
import string

def generate_password(length):
    # Define characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Prompt the user for password length
password_length = int(input("Enter the desired length for the password: "))

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")