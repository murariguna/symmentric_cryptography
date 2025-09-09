def ceaser_cipher(message):
    # Initialize the encrypted message as an empty string
    encrypted_message = ""
    #We use the ord() function to convert characters to their ASCII values and chr() to convert them back.
    for char in message:
        if char.islower(): 
            new_position = (ord(char) - ord('a') + 3) % 26
            encrypted_message += chr(new_position + ord('a'))
        elif char.isupper():  
            new_position = (ord(char) - ord('A') + 3) % 26
            encrypted_message += chr(new_position + ord('A'))
        else:
            encrypted_message += char
    
    # Output the encrypted message
    print("Encrypted message:", encrypted_message)

def monoalphabatic_cipher(message,key):
     # Initialize the encrypted message as an empty string
    encrypted_message = ""
    #We use the ord() function to convert characters to their ASCII values and chr() to convert them back.
    for char in message:
        if char.islower(): 
            new_position = (ord(char) - ord('a') + key) % 26
            encrypted_message += chr(new_position + ord('a'))
        elif char.isupper():  
            new_position = (ord(char) - ord('A') + key) % 26
            encrypted_message += chr(new_position + ord('A'))
        else:
            encrypted_message += char
    
    # Output the encrypted message
    print("Encrypted message:", encrypted_message)
def polyalphabatic_cipher(message,key):
def play_fair_cipher(message,key):
def hill_cipher(message,key):
#inputs
 
# Take user input for the message
message = input("Enter the Message: ")

# Display cipher options
print("Select a cipher type:")
print("1. Caesar Cipher")
print("2. Monoalphabetic Cipher")
print("3. Polyalphabetic Cipher")
print("4. Playfair Cipher")
print("5. Hill Cipher")
#Take user input for cipher
choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    print("Caesar Cipher selected....")
     # Get the shift key from the user
    print("THE KEY IS ALWAYS 3 IN CAESAR CIPHER")
    ceaser_cipher(message)
if choice == 2:
   print("Monoalphabatic cipher is selcted....")
   key = int(input("Enter the shift(0-26): "))
   
    
    
