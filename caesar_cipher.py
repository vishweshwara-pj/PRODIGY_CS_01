import string

# Create a list of lowercase letters from the alphabet
alpha = list(string.ascii_lowercase)

# Function to encrypt plain text using Caesar Cipher
def encrypt(plain_text, shift):
    input_text = plain_text.lower()  # Convert the text to lowercase
    output = ""  # Initialize an empty string for the encrypted result
    # Loop through each character in the input text
    for char in input_text:
        # Check if the character is a letter
        if char in alpha:
            # Find the new character after applying the shift
            output += alpha[(alpha.index(char) + shift) % 26]
        else:
            # If it's not a letter (e.g., space, punctuation), leave it unchanged
            output += char
    return output  # Return the encrypted string

# Function to decrypt cipher text using Caesar Cipher
def decrypt(cipher_text, shift):
    input_text = cipher_text.lower()  # Convert the text to lowercase
    output = ""  # Initialize an empty string for the decrypted result
    # Loop through each character in the input text
    for char in input_text:
        # Check if the character is a letter
        if char in alpha:
            # Find the original character by reversing the shift
            output += alpha[(alpha.index(char) - shift) % 26]
        else:
            # If it's not a letter, leave it unchanged
            output += char
    return output  # Return the decrypted string

# Print a welcome message to the user
print("---------Welcome to Caesar Cipher Generator----------")

# Infinite loop to get the user's choice until valid input is received
while True:
    try:
        # Ask the user whether they want to encrypt or decrypt
        choice = int(input("Encrypt? -> enter '1'\nDecrypt? -> enter '2'\n>> "))
        # Ensure the choice is either 1 (encrypt) or 2 (decrypt)
        if choice not in [1, 2]:
            raise ValueError
        break  # Exit the loop if a valid choice is made
    except ValueError:
        # Print an error message if the input is not a valid number
        print("Please enter a valid choice (1 for encryption, 2 for decryption)")

# Handle the encryption choice
if choice == 1:
    plain_text = input("\nEnter your plain text: ")  # Get the plain text from the user
    while True:
        try:
            # Ask the user for the shift value and ensure it's an integer
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            # Print an error message if the shift value is not a valid integer
            print("Please enter a valid integer for the shift value.")
    # Encrypt the text and display the result
    print("The encrypted code is ->", encrypt(plain_text, shift))

# Handle the decryption choice
elif choice == 2:
    cipher_text = input("\nEnter your cipher text: ")  # Get the cipher text from the user
    while True:
        try:
            # Ask the user for the shift value and ensure it's an integer
            shift = int(input("Enter the shift value: "))
            break
        except ValueError:
            # Print an error message if the shift value is not a valid integer
            print("Please enter a valid integer for the shift value.")
    # Decrypt the text and display the result
    print("The decrypted code is ->", decrypt(cipher_text, shift))
