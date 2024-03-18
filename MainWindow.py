import tkinter as tk
from PassChange import PasswordChange
from CardChange import CardChange


class Window:
    def __init__(self):
        self.success = None
        self.window = tk.Tk()

        self.window.resizable(width=False, height=False)
        self.window.title('Банк')
        self.window.geometry('720x620')
        self.window["bg"] = 'black'

        self.text = tk.Label(self.window, text='Главная', font=('Arial Bold', 15), fg='lime', bg='black')
        self.text.place(x=305, y=25)

        self.request = tk.Button(self.window, text='Запрос', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.request.place(x=265, y=135)

        self.deposit = tk.Button(self.window, text='Депозит', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.deposit.place(x=265, y=185)

        self.withdrawal = tk.Button(self.window, text='Снятие', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.withdrawal.place(x=265, y=235)

        self.transfer = tk.Button(self.window, text='Перевод', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.transfer.place(x=265, y=285)

        self.password = tk.Button(self.window, text='Сменить пароль', command=self.change_password, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.password.place(x=265, y=335)

        self.block = tk.Button(self.window, text='Блокировка', command=self.block, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.block.place(x=265, y=385)

        self.unblock = tk.Button(self.window, text='Разблокировка', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.unblock.place(x=265, y=435)

        self.card = tk.Button(self.window, text='Заменить карту', command=self.change_card_number, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.card.place(x=265, y=485)

        self.cancel = tk.Button(self.window, text='Удалить аккаунт', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.cancel.place(x=265, y=535)

        self.window.mainloop()

    def change_password(self):
        passChangeWindow = tk.Toplevel(self.window)
        passChangeWindow.title('Смена пароля')
        passChangeWindow.geometry('400x300')
        passChangeWindow.resizable(width=False, height=False)

        PasswordChange(passChangeWindow)
        passChangeWindow.mainloop()

    def change_card_number(self):
        cardNumberChangeWindow = tk.Toplevel(self.window)
        cardNumberChangeWindow.title('Смена пароля')
        cardNumberChangeWindow.geometry('400x300')
        cardNumberChangeWindow.resizable(width=False, height=False)

        CardChange(cardNumberChangeWindow)
        cardNumberChangeWindow.mainloop()

    def block(self):
        pass