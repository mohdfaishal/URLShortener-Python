import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("350x250") # Changes the dimensions from 350x200 to 350x250
root.title("URL Shortener")
root.configure(bg="#8ee5da")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="URL Shortener App", font="Verdana").pack(pady=10)
Entry(root, textvariable=url, width=35).pack(pady=10) # Adding width=35
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=10)
Entry(root, textvariable=url_address, width=35).pack(pady=10) # Adding width=35
Button(root, text="Copy URL", command=copyurl).pack(pady=5)

root.mainloop()
