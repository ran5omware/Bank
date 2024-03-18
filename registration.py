import tkinter as tk
from tkinter import messagebox
from OpenAccount import Database


class Registration:

    def __init__(self, window):
        self.window = window

        self.EnName = tk.Label(self.window, text='Введите ФИО')
        self.EnName.place(x=150, y=25)
        self.EnterName = tk.Entry(self.window, width=40)
        self.EnterName.place(x=85, y=55)

        self.iden = tk.Label(self.window, text='Введите идентификатор')
        self.iden.place(x=140, y=85)
        self.EnterId = tk.Entry(self.window, width=40)
        self.EnterId.place(x=85, y=115)

        self.pn = tk.Label(self.window, text='Введите номер телефона')
        self.pn.place(x=140, y=145)
        self.EnterPN = tk.Entry(self.window, width=40)
        self.EnterPN.place(x=85, y=175)

        self.pas = tk.Label(self.window, text='Введите пароль')
        self.pas.place(x=150, y=205)
        self.EnterPass = tk.Entry(self.window, width=40)
        self.EnterPass.place(x=85, y=235)

        conf = tk.Button(self.window, text='Сохранить', command=self.add_text, width=20, height=1)
        conf.place(x=130, y=285)

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
            if result == 'done':
                messagebox.showinfo("Popup", "Регистрация прошла успешно")
                self.window.destroy()
