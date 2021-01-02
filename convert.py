import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Pillow import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=250, bg='lightsteelblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def getJPG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JPG)


def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_PNG)

root.mainloop()