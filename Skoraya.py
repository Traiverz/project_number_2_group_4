import openpyxl
from tkinter import *
root = Tk()

wb = openpyxl.reader.excel.load_workbook(filename="Скорая.xlsx")
wb.active = 1
sheet = wb.active

for i in range(1,5):
    print(sheet['A' + str(i)].value,sheet['B' + str(i)].value)

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
