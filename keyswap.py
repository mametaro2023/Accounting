import tkinter as tk
from tkinter import messagebox
import keyboard
import threading
import time
import pyautogui as pgui
import sys
#from pynput import keyboard

#keyboard.add_hotkey("a",lambda: print("pressed a"),suppress=True)
#keyboard.wait("b")

#必要
what_swap = "page up"

#終了
def click_close():
    global go
    if go == True:
        messagebox.showinfo(message="You cannot close the software while key swapping is enabled")
    else:
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
root.geometry("240x220")
root.title("Key Swap")

#swap keys
swap1_key = "a"
swap2_key = "b"
#go 
go = False

#main
def check():
    global go
    global swap1_key
    global swap2_key
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
    global swap1
    global swap2
    
    if go == False:
        setup_button.config(state = tk.NORMAL)
        now_enabled.config(text="")
        
        #swap1 = "page up"
        #swap2 = "page up"
        keyboard.unremap_key(remove=swap1)
        keyboard.unremap_key(remove=swap2)

    def sp1():
        global swap2
        print(swap1,swap2)
        keyboard.press_and_release(swap2)
    def sp2():
        global swap1
        print(swap1,swap2)
        keyboard.press_and_release(swap1)
    print(go)
   
        

    if go == True:
        setup_button.config(state = tk.DISABLED)   
        swap1 = swap1_key
        swap2 = swap2_key
        swap = str(swap1 + "," + swap2)
        #keyboard.block_key(swap1)
        #keyboard.block_key(swap2)
        keyboard.remap_key(swap1,swap2)
        keyboard.remap_key(swap2,swap1)
        
    print(swap1)
    print(swap2)
    #keyboard.on_press_key(swap1, lambda _:sp1(),suppress=True)
    #keyboard.on_press_key(swap2, lambda _:sp2(),suppress=True)
        #flg = keyboard.read_key(suppress= True)
        #keyboard.add_hotkey(swap1,lambda: sp1(),suppress=True)
        #keyboard.add_hotkey(swap2,lambda: sp2(),suppress=True)

        #keyboard.wait("page down",)

        #keyboard.clear_all_hotkeys()
        #print(flg)
 


       

        



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
button = tk.Button(root, text = "Enable", font = ("",14,"bold"),command=button_push)
button.pack()

root.protocol("WM_DELETE_WINDOW", click_close)
root.mainloop()

