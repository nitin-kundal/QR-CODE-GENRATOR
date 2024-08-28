import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = data_entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter some data.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image
    img = qr.make_image(fill='black', back_color='white')

    # Convert image to Tkinter format
    img_tk = ImageTk.PhotoImage(img)

    # Update label with the new image
    img_label.config(image=img_tk)
    img_label.image = img_tk  # Keep a reference to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place widgets
tk.Label(root, text="Enter Data:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
data_entry = tk.Entry(root, width=40)
data_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate QR Code", command=generate_qr).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

img_label = tk.Label(root)
img_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()

