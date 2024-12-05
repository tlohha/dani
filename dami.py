import os
import tkinter as tk
import matplotlib.pyplot as plt
import PIL.Image, PIL.ImageTk

# Set the DISPLAY environment variable to use xvfb
os.environ['DISPLAY'] = ':99'

# Start xvfb in the background
! /usr/bin/Xvfb :99 -screen 0 1024x768x24 &

# ... (rest of your code remains the same) ...

def greet():
    greeting_label.config(text=f"Hello, {name_entry.get()}!")

# Create the main window
app = tk.Tk()
app.title("Simple Greeting App")

# Input and button
tk.Label(app, text="Enter your name:").pack(pady=5)
name_entry = tk.Entry(app)
name_entry.pack(pady=5)

greet_button = tk.Button(app, text="Greet", command=greet)
greet_button.pack(pady=5)

# Greeting label
greeting_label = tk.Label(app, text="")
greeting_label.pack(pady=5)

# Save window content as an image
app.update()  # Ensure window is fully rendered
app.deiconify()  # Make sure the window is visible
app.withdraw()  # Hide the window

app.postscript(file="myimage.ps", colormode='color')
psimage=PIL.Image.open("myimage.ps")
psimage.save("myimage.png")


# Display the image within the notebook
plt.figure(figsize=(8, 6))
img = plt.imread("myimage.png")
plt.imshow(img)
plt.axis('off')
