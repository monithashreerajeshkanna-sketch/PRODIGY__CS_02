# PRODIGY__CS_02
DESCRIPTION
A simple image encryption/decryption tool using pixel-level XOR manipulation, built in Python as part of the Prodigy Infotech Cybersecurity Internship.
Here's that content pulled from the README:

**Features**
- Browse and select any image (JPG, PNG, BMP)
- Encrypt image using a secret key number
- Decrypt image using the same key
- Live image preview inside the GUI window

**How It Works**
- Every image is made of pixels. Each pixel has 3 values: Red, Green, Blue (0–255)
- `encrypt()` function adds the key to each RGB value of every pixel
- `decrypt()` function subtracts the key to get back the original pixel values
- `% 256` ensures the values always stay between 0 and 255

**Code Explanation**
- `Image.open()` opens the selected image file
- `img.load()` reads all the pixel values of the image
- `(r + key) % 256` adds key to Red value and keeps it within range
- `filedialog.asksaveasfilename()` lets user choose where to save output image

**Technologies Used**
- Python 3.13
- Tkinter (GUI)
- Pillow 12.2.0

**How to Run**
- `py -m pip install Pillow`
- Open `Image_Encryption.py` in IDLE
- Press F5 to run
