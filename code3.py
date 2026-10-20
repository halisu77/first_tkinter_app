from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Моя первая программа, созданная с помощью пакета Tkinter")
root.iconbitmap(default="github-logo_icon-icons.com_73546.ico")
root.geometry("600x400")

btn = ttk.Button()
btn.pack()
btn["text"]="Послать текст, в котором будет написано, что до конца пар осталось какое-то количество минут"
btnText = btn["text"]
print(btnText)
# вызов главного окна с помощью метода mainloop
root.mainloop()