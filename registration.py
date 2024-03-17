import time
import tkinter as tk
from tkinter import messagebox
from OpenAccount import Database


class Registration:
    def __init__(self):
        self.window = tk.Tk()

        self.window.resizable(width=False, height=False)
        self.window.title('Банк')
        self.window.geometry('720x360')

        self.EnName = tk.Label(self.window, text='Введите ФИО')
        self.EnName.place(x=305, y=25)
        self.EnterName = tk.Entry(self.window, width=40)
        self.EnterName.place(x=220, y=55)

        self.iden = tk.Label(self.window, text='Введите идентификатор')
        self.iden.place(x=275, y=85)
        self.EnterId = tk.Entry(self.window, width=40)
        self.EnterId.place(x=220, y=115)

        self.pn = tk.Label(self.window, text='Введите номер телефона')
        self.pn.place(x=270, y=145)
        self.EnterPN = tk.Entry(self.window, width=40)
        self.EnterPN.place(x=220, y=175)

        self.pas = tk.Label(self.window, text='Введите пароль')
        self.pas.place(x=300, y=205)
        self.EnterPass = tk.Entry(self.window, width=40)
        self.EnterPass.place(x=220, y=235)

        conf = tk.Button(self.window, text='Сохранить', command=self.add_text, width=20, height=1)
        conf.place(x=265, y=265)

        self.window.mainloop()

    def add_text(self):
        name = self.EnterName.get()
        identifier = self.EnterId.get()
        phone = self.EnterPN.get()
        password = self.EnterPass.get()
        if name == '' or identifier == '' or phone == '' or password == '':
            tk.messagebox.showinfo("Ошибка", "Пустое поле")
        else:
            db = Database()
            result = db.write_info(name, identifier, phone, password)
            if result == "Готово":
                self.open_new_window()

    def open_new_window(self):
        new_window = tk.Toplevel(self.window)
        new_window.title("Успешно сохранено")
        label = tk.Label(new_window, text="Данные успешно сохранены!", pady=20)
        label.pack()
        ok = tk.Button(new_window, text='Ok', command=self.close_window)
        ok.pack()

    def close_window(self):
        self.window.destroy()
        return 'done'
