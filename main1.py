import tkinter as tk
from tkinter import *

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
            color = Menu(helpmenu, tearoff=0)
            color.add_command(command="", label="Авто оформление 1")
            color.add_command(label="Авто оформление 2", command=self.oforlmlenie)
            color.add_command(label="Авто оформление 2")
            helpmenu.add_cascade(label="Цветовое оформление", menu=color)

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

if __name__ == "__main__":
    root = tk.Tk()
    main = Main(root)
    main.pack()
    root.title("Скорая помощь")
    root.geometry("280x120")
    root.mainloop()