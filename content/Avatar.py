import tkinter as tk

from tkinter import ttk

print("This is the output (Console) where your link come out!")

def UpdateLink():
    f = entry.get() 
    a = f'rbxthumb://type=Avatar&id={f}&w=180&h=180'
    print("Copy this link down bellow!")
    print(a)

window = tk.Tk()

window.title('Avatar')

window.geometry('300x190')

window.resizable(0,0)

window.iconbitmap('icon.ico')

label = ttk.Label(master=window, text='Avatar mode')
label2 = ttk.Label(master=window, text='Roblox Player ID down bellow')
entry = ttk.Entry(master=window)
button = ttk.Button(master=window, text='Generate', command=UpdateLink)
link = ttk.Label(master=window, text='Result in output! (Console)')

label.pack(pady=10)
label2.pack()
entry.pack(pady=10)
button.pack()
link.pack(pady=13)

window.mainloop()
