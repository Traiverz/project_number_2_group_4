import tkinter as tk
from tkinter import *

#Создаём главное меню и объекты на нём
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def Dest(self):
        root.destroy();

    def init_main(self):

            mainmenu = Menu(root)
            root.config(menu=mainmenu)

            filemenu = Menu(mainmenu, tearoff=0)
            filemenu.add_command(label="Сохранить")
            filemenu.add_command(label="Выход",command = self.Dest)

            helpmenu = Menu(mainmenu, tearoff=0)
            helpmenu.add_command(label="Полноэкранный режим")
            helpmenu.add_command(label="Оконный режим")
            helpmenu.add_command(label="Цветовое оформление")
            color = Menu(helpmenu, tearoff=0)
            helpmenu.add_cascade(label="Цветовое оформление",menu = helpmenu )

            helpmenu2 = Menu(mainmenu, tearoff=0)
            helpmenu2.add_command(label="Справка")
            helpmenu2.add_command(label="Информация",command = self.vizov_inf)

            mainmenu.add_cascade(label="Файл",menu=filemenu)
            mainmenu.add_cascade(label="Вид",menu=helpmenu)
            mainmenu.add_cascade(label="О программе", menu=helpmenu2)

            btn_svedenya = tk.Button(text='Список вызовов\nвсех бригад', compound=tk.TOP, width = 16, command = self.v_inf)
            btn_svedenya.place(x=10, y=10)
            btn_ex = tk.Button(text='Сведения о бригаде\nна дату', compound=tk.TOP, width=16)
            btn_ex.place(x=150, y=10)
            btn_vizov = tk.Button(text='Сведения о самом\nдлительном вызове', compound=tk.TOP, width = 16)
            btn_vizov.place(x=10, y=70)
            btn_brigada = tk.Button( text = 'Сведения о самом\n коротком вызове', compound = tk.TOP, width = 16)
            btn_brigada.place(x=150, y=70)


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
        self.geometry('430x220')
        self.resizable(False, False)

        label_name = tk.Label(self, text="Скорая помощь", font =('Times New Roman', 25))
        label_name.place(x=100, y=10)
        label_info = tk.Label(self,text="Данную программу разрабатывали:\n Буряк Роман,\nСахаров Алексей,\n Сыздыков Раимбек,\n Шамсутдинов Влад,\n с использованием python и Tkinter \n для контроля бригад скорой помощи")
        label_info.place(x=110, y=70)


#Создаём форму где будет храниться информация о вызовах
class viz_info(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.v_info()

    def v_info(self):
        self.title('Вызовы')
        self.geometry('600x250')
        self.resizable(False, False)

        label_name = tk.Label(self, text="Введите дату")
        label_name.place(x=10, y=6)
        text_info = tk.Entry(self)
        text_info.place(x=100, y=10)
        btn_ent = tk.Button(self,text='Ввод', compound=tk.TOP, width=16)
        btn_ent.place(x=260, y=10)
        box = Listbox(self, selectmode = EXTENDED,width = 90)
        box.place(x=10, y=40)

#Создаём главное меню, задаём его размеры и выводим компоненты
if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    main.pack()
    root.title("Скорая помощь")
    root.geometry("280x120")
    root.mainloop()
