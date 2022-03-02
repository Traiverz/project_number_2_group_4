import tkinter as tk
from tkinter import *

#Создаём главное меню и объекты на нём
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
            toolbar = tk.Frame(bg='#d7d8e0', bd=2)
            toolbar.pack(side=tk.TOP, fill=tk.X)
            # Не мог сделать
            btn_open_dialog = tk.Button(toolbar, text='О программе', bg='#d7d8e0', compound=tk.TOP, command = self.vizov_inf)
            btn_open_dialog.pack(side=tk.LEFT)
            btn_svedenya = tk.Button(text='Список вызовов\nвсех бригад', compound=tk.TOP, width = 16, command = self.v_inf)
            btn_svedenya.pack()
            btn_vizov = tk.Button(text='Сведения о самом\nдлительном вызове', compound=tk.TOP, width = 16)
            btn_vizov.pack()
            btn_brigada = tk.Button(text='Сведения о бригаде\nпо дате', compound=tk.TOP, width = 16)
            btn_brigada.pack()
            btn_ex = tk.Button(text='Выход', compound=tk.TOP, width = 16)
            btn_ex.pack()

    def vizov_inf(self):
        info()

    def v_inf(self):
        viz_info()

#Создаём форму на которой будет информация о программе
class info(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_info()

    def init_info(self):
        self.title('Информация о программе')
        self.geometry('400x220')
        self.resizable(False, False)

        label_name = tk.Label(self, text="Скорая помощь", font =('Times New Roman', 25))
        label_name.place(x=100, y=10)
        label_info = tk.Label(self,text="Программа была разработана 4-ой минигруппой,\n с использованием python и Tkinter \n для контроля бригад скорой помощи")
        label_info.place(x=70, y=70)

#Создаём форму где будет храниться информация о вызовах
class viz_info(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.v_info()

    def v_info(self):
        self.title('Вызовы')
        self.geometry('600x600')
        self.resizable(False, False)

        label_name = tk.Label(self, text="Введите дату")
        label_name.place(x=10, y=6)
        text_info = tk.Entry(self)
        text_info.place(x=100, y=10)
        btn_ent = tk.Button(self,text='Ввод', compound=tk.TOP, width=16)
        btn_ent.place(x=260, y=10)
        box = Listbox(self, selectmode = EXTENDED,width = 100)
        box.place(x=0, y=40)

#Создаём главное меню, задаём его размеры и выводим компоненты
if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    main.pack()
    root.title("Скорая помощь")
    root.geometry("250x200")
    root.mainloop()
