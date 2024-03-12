import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Frame Example")

# Create a Frame widget
frame = tk.Frame(root, bd=5)

# Pack the Frame into the root window
frame.pack(padx=10, pady=10)

# Adding widgets to the frame
label = tk.Label(frame, text="I'm inside a Frame!")
label.pack(padx=5, pady=5)

button = tk.Button(frame, text="Click Me")
button.pack(padx=5, pady=5)

# Run the application
root.mainloop()
