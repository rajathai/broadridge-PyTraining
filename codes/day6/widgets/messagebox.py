import tkinter as tk
import sqlite3


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    # Insert into database
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()

    # Clear the entry fields
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


def show_contacts():
    # Connect to database and fetch contacts
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    records = cursor.fetchall()
    conn.close()

    # Create a new window to show contacts
    contact_window = tk.Toplevel()
    contact_window.title("Contacts")

    # Display each contact in the new window
    for idx, record in enumerate(records):
        tk.Label(contact_window, text=f"{record[1]} - {record[2]}").grid(
            row=idx, column=0
        )


# Set up the main window
root = tk.Tk()
root.title("Contact Book")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Add 'File' menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Show Contacts", command=show_contacts)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create and pack widgets for adding contacts
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

# Run the application
root.mainloop()
