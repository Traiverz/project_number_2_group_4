from tkinter import *
root = Tk()

l1 = Label(text = "Логин")
en1 = Entry()
l2 = Label(text = "Пароль")
en2 = Entry()
but1 = Button(text = "Войти")

l1.pack()
en1.pack()
l2.pack()
en2.pack()
but1.pack()

root.mainloop()
