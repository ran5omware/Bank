from random import randint
import sqlite3


class Database:
    def __init__(self, db_name='main.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                        name TEXT,
                        identifier TEXT,
                        phoneNumber TEXT,
                        password TEXT,
                        cardNumber TEXT
                    )""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS accounts (
                        cardNumber TEXT,
                        demand_balance INTEGER,
                        fixed_balance INTEGER,
                        freeze TEXT
                    )""")
        self.conn.commit()

    def write_info(self, name, identifier, phoneNumber, password):
        try:
            cur = self.cur
            conn = self.conn

            cur.execute("SELECT cardNumber FROM users")
            numbers = cur.fetchall()

            cardNumber = ' '.join([str(randint(1000, 9999)) for _ in range(4)])
            while cardNumber in numbers:
                cardNumber = ' '.join([str(randint(1000, 9999)) for _ in range(4)])

            cur.execute(
                "INSERT INTO users (name, identifier, phoneNumber, password, cardNumber) VALUES (?, ?, ?, ?, ?)",
                (name, identifier, phoneNumber, password, cardNumber))
            cur.execute("INSERT INTO accounts (cardNumber, demand_balance, fixed_balance, freeze) VALUES (?, ?, ?, ?)",
                        (cardNumber, 0, 0, "Разблокирована"))
            conn.commit()
            return "Готово"
        except sqlite3.Error as e:
            print("Ошибка при записи в базу данных:", e)
            return "Ошибка"
