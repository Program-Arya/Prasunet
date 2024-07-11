alphabets_lower = list('abcdefghijklmnopqrstuvwxyz')
alphabets_upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                index = alphabets_lower.index(char)
                encrypted_char = alphabets_lower[(index + shift) % 26]
            else:
                index = alphabets_upper.index(char)
                encrypted_char = alphabets_upper[(index + shift) % 26]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                index = alphabets_lower.index(char)
                decrypted_char = alphabets_lower[(index - shift) % 26]
            else:
                index = alphabets_upper.index(char)
                decrypted_char = alphabets_upper[(index - shift) % 26]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Main program
while True:
    print("Caesar Cipher Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")

        if any(char.isdigit() for char in message):
            print("Error: Message cannot contain digits.")
            continue
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)

    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        if any(char.isdigit() for char in message):
            print("Error: Message cannot contain digits.")
            continue
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
