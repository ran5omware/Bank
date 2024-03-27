import tkinter as tk
from PassChange import PasswordChange
from CardChange import CardChange
from Lock import Lock
from Unlock import Unlock
from OpenAccount import Database
from Deposit import Deposit
from Transfer import Transfer
from Request import Balance


class Window:
    def __init__(self, current_user):
        self.success = None
        self.window = tk.Tk()

        self.window.resizable(width=False, height=False)
        self.window.title('Банк')
        self.window.geometry('720x620')
        self.window["bg"] = 'black'

        self.user = current_user
        db = Database()
        self.cur = db.cur
        self.conn = db.conn

        self.text = tk.Label(self.window, text='Главная', font=('Arial Bold', 15), fg='lime', bg='black')
        self.text.place(x=305, y=25)

        self.request = tk.Button(self.window, text='Запрос', command=self.request, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.request.place(x=265, y=135)

        self.deposit = tk.Button(self.window, text='Депозит', command=self.deposit, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.deposit.place(x=265, y=185)

        self.withdrawal = tk.Button(self.window, text='Снятие', font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.withdrawal.place(x=265, y=235)

        self.transfer = tk.Button(self.window, text='Перевод', command=self.transfer, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.transfer.place(x=265, y=285)

        self.password = tk.Button(self.window, text='Сменить пароль', command=self.change_password, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.password.place(x=265, y=335)

        self.lock = tk.Button(self.window, text='Блокировка', command=self.block, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.lock.place(x=265, y=385)

        self.unlock = tk.Button(self.window, text='Разблокировка', command=self.unblock, font=('Georgia', 10), fg='white', bg='gray', width=20, height=1)
        self.unlock.place(x=265, y=435)

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
        cardNumberChangeWindow.title('Замена карты')
        cardNumberChangeWindow.geometry('400x300')
        cardNumberChangeWindow.resizable(width=False, height=False)

        CardChange(cardNumberChangeWindow)
        cardNumberChangeWindow.mainloop()

    def block(self):
        self.cur.execute("SELECT bankNumber FROM users WHERE identifier=?", (self.user,))
        l = Lock()
        l.lock(self.cur.fetchone()[0])

    def unblock(self):
        unlockWindow = tk.Toplevel(self.window)
        unlockWindow.title('Разблокировка аккаунта')
        unlockWindow.geometry('400x300')
        unlockWindow.resizable(width=False, height=False)

        Unlock(unlockWindow)
        unlockWindow.mainloop()

    def request(self):
        requestWindow = tk.Toplevel(self.window)
        requestWindow.title('Выписка баланса')
        requestWindow.geometry('400x300')
        requestWindow.resizable(width=False, height=False)

        self.cur.execute("SELECT bankNumber FROM users WHERE identifier=?", (self.user,))
        bankNumber = self.cur.fetchone()[0]
        Balance(requestWindow, bankNumber)
        requestWindow.mainloop()

    def deposit(self):
        depositWindow = tk.Toplevel(self.window)
        depositWindow.title('Депозит средств')
        depositWindow.geometry('400x300')
        depositWindow.resizable(width=False, height=False)

        self.cur.execute("SELECT bankNumber FROM users WHERE identifier=?", (self.user,))
        bankNumber = self.cur.fetchone()[0]
        Deposit(depositWindow, bankNumber)
        depositWindow.mainloop()

    def transfer(self):
        tranferWindow = tk.Toplevel(self.window)
        tranferWindow.title('Депозит средств')
        tranferWindow.geometry('400x300')
        tranferWindow.resizable(width=False, height=False)

        self.cur.execute("SELECT bankNumber FROM users WHERE identifier=?", (self.user,))
        bankNumber = self.cur.fetchone()[0]
        Transfer(tranferWindow, bankNumber)
        tranferWindow.mainloop()


if __name__ == '__main__':
    Window('2')
