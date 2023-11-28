import tkinter as tk
from tkinter import simpledialog, messagebox

# Function to handle the purchase and generate receipt
def handle_purchase():
    email = user_email.get()
    color = color_var.get()
    size = size_var.get()
    quantity = quantity_var.get()

    # Mock receipt generation
    receipt = f"Receipt:\nEmail: {email}\nT-Shirt Color: {color}\nSize: {size}\nQuantity: {quantity}"
    print(receipt)

    # Clear inputs for next entry
    user_email.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("T-Shirt Purchase")

# Email input
tk.Label(root, text="Enter your email:").pack()
user_email = tk.Entry(root)
user_email.pack()

# T-shirt color selection
color_var = tk.StringVar()
color_var.set("Red")
tk.Label(root, text="Choose T-shirt color:").pack()
for color in ["Red", "Blue", "Green", "Yellow"]:
    tk.Radiobutton(root, text=color, variable=color_var, value=color).pack()

# T-shirt size selection
size_var = tk.StringVar()
size_var.set("Large")
tk.Label(root, text="Choose T-shirt size:").pack()
for size in ["Large", "Medium", "Small"]:
    tk.Radiobutton(root, text=size, variable=size_var, value=size).pack()

# Quantity selection
quantity_var = tk.StringVar()
quantity_var.set("1")
tk.Label(root, text="Choose quantity:").pack()
for quantity in ["1", "5", "10"]:
    tk.Radiobutton(root, text=quantity, variable=quantity_var, value=quantity).pack()

# Submit button
submit_button = tk.Button(root, text="Purchase", command=handle_purchase)
submit_button.pack()

# Start the GUI event loop
root.mainloop()
