# s24028
# 画像ファイルを表示するアプリケーション

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

imageLabel = tk.Label(text="画像表示アプリバージョン2.0")
btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel.pack()
btn.pack()

tk.mainloop()
