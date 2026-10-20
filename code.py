# импортируем модуль tkinter
from tkinter import *
from tkinter import ttk

#создаём главное окно
root = Tk()
# создаём заголовок для окна
root.title("Моя первая программа, созданная с помощью пакета Tkinter")
root.iconbitmap(default="github-logo_icon-icons.com_73546.ico")
# задаём размеры для окна
root.geometry("600x400")

# создаём леёбл для вывода текстового сообщения
label = Label(text="Привет, мир!")
# размещаем лейбл с помощью метода pack
label.pack()

btn = ttk.Button()
btn.pack()
btn["text"]="Послать текст, в котором будет написано, что до конца пар осталось какое-то количество минут"
btnText = btn["text"]
print(btnText)
# вызов главного окна с помощью метода mainloop
root.mainloop()