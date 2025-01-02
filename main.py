from tkinter import *
import qrcode
import os

# Ensure the "Qrcode" directory exists
if not os.path.exists("Qrcode"):
    os.makedirs("Qrcode")

root = Tk()
root.title("QR Code Generator")
root.geometry("1000x500")
root.config(bg="#38c0ec")
root.resizable(False, False)

# Icon image
try:
    image_icon = PhotoImage(file="icon.png")
    root.iconphoto(False, image_icon)
except TclError:
    print("Warning: 'icon.png' not found. Skipping icon setup.")

# Function to generate QR code
def generate():
    name = title.get()
    link = link_entry.get()
    if not name or not link:
        print("Error: Title and Link fields must not be empty.")
        return

    qr_path = f"Qrcode/{name}.png"
    qr = qrcode.make(link)
    qr.save(qr_path)

    try:
        # Update the QR code image
        qr_image = PhotoImage(file=qr_path)
        image_view.config(image=qr_image)
        image_view.image = qr_image  # Prevent garbage collection
    except TclError:
        print(f"Error: Could not load the QR code image at {qr_path}.")

# Label and Entry for title
Label(root, text="Title", fg="white", bg="#38c0ec", font=15).place(x=50, y=170)

title = Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

# Label and Entry for the link
Label(root, text="Enter the Link", fg="white", bg="#38c0ec", font=15).place(x=50, y=250)

link_entry = Entry(root, width=28, font="arial 15")
link_entry.place(x=50, y=280)

# Button to generate QR code
Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=330)

# Label to display QR code
image_view = Label(root, bg="#38c0ec")
image_view.pack(padx=50, pady=10, side=RIGHT)

root.mainloop()
