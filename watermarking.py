import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image

file1 = file2 = None


def watermark():
    global file1, file2
    # make sure both images are selected
    if file1 and file2:
        # make sure the loaded images support transparency
        logo_image = Image.open(file2).convert("RGBA")
        background_image = Image.open(file1).convert("RGBA")

        logo_width, logo_height = logo_image.size
        background_width, background_height = background_image.size

        if logo_width > background_width or logo_height > background_height:
            # Use thumbnail() to keep the image aspect ratio
            logo_image.thumbnail((background_width, background_height))

        logo_x = 0
        logo_y = 0

        background_image.paste(logo_image, (logo_x, logo_y), mask=logo_image)
        background_image.show()


def open_file():
    global file1
    file1 = filedialog.askopenfilename(initialdir='images')


def open_file_logo():
    global file2
    file2 = filedialog.askopenfilename(initialdir='images')


window = tk.Tk()
window.title("WaterMarker")
window.geometry('300x200')
window.config(padx=20, pady=20)

label = ttk.Label(window, text="Select the image", font=("Arial", 25))
label.pack()

button1 = ttk.Button(window, text="Select Image", command=open_file)
button1.pack()

button2 = ttk.Button(window, text="Select Image Logo", command=open_file_logo)
button2.pack()

button3 = ttk.Button(window, text="Show Watermark Image", command=watermark)
button3.pack()

window.mainloop()
