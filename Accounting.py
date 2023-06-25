import tkinter as tk
import tkinter.ttk as ttk
import datetime as dt

#GUI作成
root = tk.Tk()
root.geometry("240x240")
root.title("Key Swap")

now = dt.datetime.now()
weekday = int(now.weekday())
weeklist = list(["月","火","水","木","金","土","日",])
week = str("("+ weeklist[weekday] + ")")
today = now.strftime("%Y年%m月%d日")

label1 = tk.Label(root,text= today + week , font=("",20))
label1.place(x=20,y=20)

jikken = ["a","v","c"]
label2 = ttk.Combobox(height = 5, width = 20, textvariable = tk.StringVar(),
                      values = jikken, font = ("",16)
                      )

label2.place(x=50,y=50)

root.mainloop()
