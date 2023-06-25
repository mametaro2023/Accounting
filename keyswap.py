import tkinter as tk
from tkinter import messagebox
import keyboard
import threading
import time
import pyautogui as pgui
import sys


#終了
def click_close():
    global go
    button.config(text = "Enable")
    now_enabled.config(text="")
    go = False
    
    global swap1_key
    global swap2_key
    if swap1_key == "?" or swap2_key == "?":
        messagebox.showinfo(message="You cannot close the software while you are changing swap keys.")
    elif messagebox.askokcancel(message="Are you sure to close?"):
        #print("closed")
        root.destroy()
        sys.exit()
    

#GUI作成
root = tk.Tk()
root.geometry("240x240")
root.title("Key Swap")

#swap keys
swap1_key = "a"
swap2_key = "b"
#go 
go = False

#main
def check():
    global go
    if button["text"] == "Enable":
        button.config(text = "Disable")
        now_enabled.config(text = "NOW ENABLED!" ,)
        go = True
    elif button["text"] == "Disable":
        button.config(text = "Enable")
        now_enabled.config(text="")
        go = False



#メイン処理
def main():
    global go
    if go == True:
        setup_button.config(state = tk.DISABLED)   
        swap1 = swap1_key
        swap2 = swap2_key
        keyboard.block_key(swap1)
        keyboard.block_key(swap2)
        
        while True:
            # print(go)
            if go == False:
                break
            if keyboard.is_pressed(swap1):
                pgui.typewrite(swap2)
            if keyboard.is_pressed(swap2):
                pgui.typewrite(swap1)
            
        keyboard.unhook_all()
        setup_button.config(state = tk.NORMAL)  

#push
def button_push():
        check()

        thread3 = threading.Thread(target = main)
        thread3.start()

def swap_keys():
    button.config(state = tk.DISABLED)
    global swap1_key
    global swap2_key
    swap1_key = "?"
    swap2_key = "?"
    label3.config(text = swap1_key + " ←→ " + swap2_key)
    swap1_key = keyboard.read_key()
    label3.config(text = swap1_key + " ←→ " + swap2_key)
    time.sleep(0.2)
    swap2_key = keyboard.read_key()
    label3.config(text = swap1_key + " ←→ " + swap2_key)
    button.config(state = tk.NORMAL)

def change_swap_keys():
    thread1 = threading.Thread(target = swap_keys)
    thread1.start()


label1 = tk.Label(root,text="Swap Any Key You Like", font=("",14), )
label1.pack()

label2 = tk.Label(root,text = "Key Config:", font=("",10))
label2.pack()

#何をスワップするか
label3 = tk.Label(root, text = swap1_key + " ←→ " + swap2_key, font=("",20))
label3.pack()

#スワップするキーの変更
setup_button = tk.Button(root, text = "change swap keys",font=("", 14),command=change_swap_keys)
setup_button.pack()

#注意
now_enabled = tk.Label(root, text = "", fg = "red", font = ("",20,"bold"))
now_enabled.pack(pady=10)

#実行
button = tk.Button(root, text = "Enable", font = ("",20,"bold"),command=button_push)
button.pack()

root.protocol("WM_DELETE_WINDOW", click_close)
root.mainloop()

