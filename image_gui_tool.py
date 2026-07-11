import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

selected_file = ""

def browse_image():
    global selected_file
    selected_file = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if selected_file:
        file_label.config(text=f"Selected File:\n{selected_file}")
        show_preview(selected_file)

def show_preview(path):
    img = Image.open(path)
    img.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(img)
    preview_label.config(image=photo)
    preview_label.image = photo

def process_image(mode):
    global selected_file
    if not selected_file:
        messagebox.showerror("Error", "Please browse and select an image first.")
        return
    try:
        key = int(key_entry.get())
        if key < 1 or key > 255:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid key number between 1 and 255.")
        return

    img = Image.open(selected_file).convert("RGB")
    arr = np.array(img)
    result = np.bitwise_xor(arr, key)
    output_img = Image.fromarray(result.astype('uint8'), 'RGB')

    folder = os.path.dirname(selected_file)
    filename = os.path.splitext(os.path.basename(selected_file))[0]
    suffix = "_encrypted" if mode == "encrypt" else "_decrypted"
    output_path = os.path.join(folder, f"{filename}{suffix}.png")

    output_img.save(output_path)
    show_preview(output_path)
    messagebox.showinfo("Success", f"Saved to:\n{output_path}")

# ---------- GUI Layout ----------
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("400x600")
root.configure(bg="#1e1e2f")

title_label = tk.Label(root, text="🔒 Image Encryption Tool", font=("Arial", 16, "bold"),
                        bg="#1e1e2f", fg="white")
title_label.pack(pady=15)

browse_btn = tk.Button(root, text="📁 Browse Image", command=browse_image,
                        bg="#7ba7d9", font=("Arial", 11, "bold"))
browse_btn.pack(pady=5)

file_label = tk.Label(root, text="Selected File:\nNone", bg="#1e1e2f", fg="white", wraplength=350)
file_label.pack(pady=5)

key_label = tk.Label(root, text="Enter Key (Number):", bg="#1e1e2f", fg="white")
key_label.pack(pady=(15, 0))

key_entry = tk.Entry(root, justify="center", font=("Arial", 12))
key_entry.pack(pady=5)

encrypt_btn = tk.Button(root, text="🔒 Encrypt Image", command=lambda: process_image("encrypt"),
                         bg="#9be89b", font=("Arial", 11, "bold"))
encrypt_btn.pack(pady=8, fill="x", padx=60)

decrypt_btn = tk.Button(root, text="🔓 Decrypt Image", command=lambda: process_image("decrypt"),
                         bg="#f79c9c", font=("Arial", 11, "bold"))
decrypt_btn.pack(pady=5, fill="x", padx=60)

preview_label = tk.Label(root, bg="#1e1e2f")
preview_label.pack(pady=20)

root.mainloop()