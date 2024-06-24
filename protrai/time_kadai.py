#s24028 Akira Yamada
#8行目　時間を常に更新するためにもっとも必要なループ文

import tkinter as tk
import datetime

def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y/%m/%d %H:%M:%S")
    lbl.config(text=current_time)
    root.after(950,update_time)

root = tk.Tk()
root.title("現在の時刻")

lbl = tk.Label()
lbl.config(text="",font=("A-OTF UD新ゴ Pr6N M",20))
lbl.pack()

update_time()

root.mainloop()