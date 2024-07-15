import numpy as np
from PIL import Image

def encrypt_image(image_path, key):
    print("Encrypting image...")
    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Apply the encryption operation: swap R and B values, and add the key to G
    encrypted_array = image_array.copy()
    encrypted_array[:, :, 0] = image_array[:, :, 2]  # Swap R and B values
    encrypted_array[:, :, 2] = image_array[:, :, 0]
    encrypted_array[:, :, 1] = np.clip(image_array[:, :, 1] + key, 0, 255).astype(np.uint8)  # Add key to G

    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array)

    # Save the encrypted image to a new file
    encrypted_image.save("encrypted_image.png")
    print("Encryption complete!")

def decrypt_image(encrypted_image_path, key):
    print("Decrypting image...")
    # Open the encrypted image using PIL
    encrypted_image = Image.open(encrypted_image_path)

    # Convert the encrypted image to a numpy array
    encrypted_array = np.array(encrypted_image)

    # Apply the decryption operation: swap R and B values, and subtract the key from G
    decrypted_array = encrypted_array.copy()
    decrypted_array[:, :, 0] = encrypted_array[:, :, 2]  # Swap R and B values
    decrypted_array[:, :, 2] = encrypted_array[:, :, 0]
    decrypted_array[:, :, 1] = np.clip(encrypted_array[:, :, 1] - key, 0, 255).astype(np.uint8)  # Subtract key from G

    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array)

    # Save the decrypted image to a new file
    decrypted_image.save("decrypted_image.png")
    print("Decryption complete!")

# Example usage:
image_path = "/root/Desktop/img.jpg"
key = 123  # Choose a secret key for encryption

encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)
