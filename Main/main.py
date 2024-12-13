#Main Page
#This Page will and is the Hub for all features.
import tkinter as tk
from tkinter import PhotoImage
from tkinter import Toplevel
from PIL import Image, ImageTk
import runpy

class EntryFormApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Momentum")
        
        # Use Pillow to open the .ico file
        img = Image.open('Main\icons\icon.ico')

        # Convert the image to PhotoImage (Tkinter format)
        tk_img = ImageTk.PhotoImage(img)

        # Set the window icon using PhotoImage
        root.iconphoto(True, tk_img)
        
        # Set window size
        root.geometry('400x300')
        
        # Create a button to open the entry form
        self.open_button = tk.Button(self.root, text="Open Entry Form", command=self.open_entry_form)
        self.open_button.pack(pady=20)

    def open_entry_form(self):        
        # Run the entry.py file inside the new window
        try:
            runpy.run_path("Main/Forms/entry.py")  # Run entry.py as if it's a standalone script
        except FileNotFoundError:
            print("File not found.")
            
# Create the main window
root = tk.Tk()
app = EntryFormApp(root)

# Run the Tkinter event loop
root.mainloop()