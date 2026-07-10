from PIL import Image
import numpy as np
import os

def encrypt_decrypt(image_path, output_path, key):
    """
    Encrypts or decrypts an image using pixel-level XOR.
    Since XOR is symmetric, the same function and key
    both encrypts and decrypts the image.
    """
    img = Image.open(image_path)
    img = img.convert("RGB")
    arr = np.array(img)

    result = np.bitwise_xor(arr, key)

    output_img = Image.fromarray(result.astype('uint8'), 'RGB')
    output_img.save(output_path)
    print(f"Success! Saved to: {output_path}")

def main():
    print("=== Pixel Manipulation Image Encryption Tool ===")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Choose an option (1 or 2): ").strip()

    image_path = input("Enter the full path of the image: ").strip('"')

    if not os.path.exists(image_path):
        print("Error: File not found. Check the path and try again.")
        return

    try:
        key = int(input("Enter a key (a number between 1 and 255): "))
        if key < 1 or key > 255:
            print("Key must be between 1 and 255.")
            return
    except ValueError:
        print("Invalid key. Must be a number.")
        return

    folder = os.path.dirname(image_path)
    filename = os.path.splitext(os.path.basename(image_path))[0]

    if choice == "1":
        output_path = os.path.join(folder, f"{filename}_encrypted.png")
    elif choice == "2":
        output_path = os.path.join(folder, f"{filename}_decrypted.png")
    else:
        print("Invalid choice.")
        return

    encrypt_decrypt(image_path, output_path, key)

if __name__ == "__main__":
    main()