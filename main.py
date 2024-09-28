import requests
import io
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from ttkbootstrap import Style

# Create the main window
root = tk.Tk()
root.title("Image Generator")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)
style = Style(theme="sandstone")

# Global variable to store the image URL
image_url = None

# Define a function to retrieve and display an image based on the entered category
def display_image():
    global image_url
    category = category_entry.get().strip()  # Get the text from the entry box
    if category:  # Check if the entry is not empty
        # Make a request to the Unsplash API to get a random image
        url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
        data = requests.get(url).json()
        img_data = requests.get(data["urls"]["regular"]).content
        
        # Store the image URL for downloading
        image_url = data["urls"]["regular"]

        photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
        label.config(image=photo)
        label.image = photo

# Function to download the displayed image
def download_image():
    if image_url:  # Check if an image URL is available
        img_data = requests.get(image_url).content
        with open("downloaded_image.jpg", "wb") as img_file:
            img_file.write(img_data)
        messagebox.showinfo("Download Complete", "Image downloaded successfully as 'downloaded_image.jpg'.")
    else:
        messagebox.showwarning("No Image", "Please generate an image first.")

# Create the GUI elements
def create_gui():
    global category_entry, generate_button, download_button, label

    # Create a label and entry for the image category
    tk.Label(root, text="Enter image category:").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_entry = tk.Entry(root, width=30)
    category_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Create buttons for generating the image and downloading it
    generate_button = ttk.Button(text="Generate Image", command=display_image)
    generate_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    download_button = ttk.Button(text="Download Image", command=download_image)
    download_button.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    # Make the columns/rows expandable
    root.columnconfigure([0, 1, 2, 3], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    create_gui()