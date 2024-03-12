import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Widget with Scrollbar")

# Create a Text widget
text_widget = tk.Text(root, height=10, width=40, wrap=tk.WORD)

# Create a Scrollbar and set it to text_widget
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
text_widget.configure(yscrollcommand=scrollbar.set)

# Pack Scrollbar and Text widget
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Function to retrieve text
def retrieve_text():
    print(text_widget.get("1.0", tk.END))


# Create a Button to retrieve text
submit_button = tk.Button(root, text="Submit", command=retrieve_text)
submit_button.pack()

# Run the application
root.mainloop()
