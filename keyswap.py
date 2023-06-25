import tkinter as tk
from tkinter import messagebox
import keyboard
import threading
import time
import sys
import subprocess
import os
#from pynput import keyboard

#keyboard.add_hotkey("a",lambda: print("pressed a"),suppress=True)
#keyboard.wait("b")

#必要
filepath = "keyswap\keyswap_setting.txt"
what_swap = "page up"
try:
    os.mkdir("keyswap")
    cmd = ["attrib", "+H", "keyswap"]
    subprocess.run(cmd)
except FileExistsError:
    pass
try:
    with open(filepath, "r") as f:
        swapdata = f.readlines()
        #swap keys
        swap1_key = swapdata[0].rstrip("\n")
        swap2_key = swapdata[1].rstrip("\n")
        f.close()
except FileNotFoundError:
    swap1_key = "a"
    swap2_key = "b"

#終了
def click_close():
    global go
    if go == True:
        messagebox.showinfo(message="キー入れ替え中はソフトを閉じることができません。")
    else:
        button.config(text = "有効化")
        now_enabled.config(text="")
        go = False
        
        global swap1_key
        global swap2_key
        global filepath
        if swap1_key == "?" or swap2_key == "?":
            messagebox.showinfo(message="入れ替えキー設定中はソフトを閉じることができません。")
        elif messagebox.askokcancel(message="本当に閉じますか？", detail="現在の入れ替えキーが保存されます。"):
            swapkeylist = [swap1_key + "\n" ,swap2_key + "\n"]
            with open(filepath, "w") as f:
                f.writelines(swapkeylist)
                f.close()
            #print("closed")
            root.destroy()
            sys.exit()
    

#GUI作成
root = tk.Tk()
root.geometry("240x220")
root.title("Key Swap")


#go 
go = False

#main
def check():
    global go
    global swap1_key
    global swap2_key
    if button["text"] == "有効化":
        button.config(text = "無効化")
        now_enabled.config(text = "現在有効" ,)
        go = True
    elif button["text"] == "無効化":
        button.config(text = "有効化")
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
        #swap = str(swap1 + "," + swap2)
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


label1 = tk.Label(root,text="任意のキーを入れ替えます", font=("",14), )
label1.pack()

label2 = tk.Label(root,text = "キー設定:", font=("",10))
label2.pack()

#何をスワップするか
label3 = tk.Label(root, text = swap1_key + " ←→ " + swap2_key, font=("",20))
label3.pack()

#スワップするキーの変更
setup_button = tk.Button(root, text = "入れ替えキー変更",font=("", 14),command=change_swap_keys)
setup_button.pack()

#注意
now_enabled = tk.Label(root, text = "", fg = "red", font = ("",20,"bold"))
now_enabled.pack(pady=10)

#実行
button = tk.Button(root, text = "有効化", font = ("",14,"bold"),command=button_push)
button.pack()

root.protocol("WM_DELETE_WINDOW", click_close)
root.mainloop()

