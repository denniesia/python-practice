import threading


class BankAccount:
    def __init__(self, initial_balance:int):
        self.balance = initial_balance
        self.open = True
        self.lock = threading.Lock()

    def __check_if_account_is_open(self):
        if not self.open:
            raise ValueError("Account is not open")

    def __check_ammount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must greater than zero")

    def deposit(self, amount):
        self.__check_if_account_is_open()

        self.__check_ammount(amount)

        with self.lock:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}".)

    def withdraw(self, amount):
        self.__check_if_account_is_open()

        self.__check_ammount(amount)

        with self.lock:
            self.balance -= amount
            print(f"Withdrawed {amount}. New balance: {self.balance}".)

    def get_balance(self):
        self.__check_if_account_is_open()
        with self.lock:
            return f"Current balance: {self.balance}"

    def close_account(self):
        self.__check_if_account_is_open()

        with self.lock:
            self.open = False
            print(f"Account has been closed.")

    def open_account(self):
        with self.lock:
            if self.open:
                raise ValueError("Account is open")
            self.open = True
            print(f"Account has been opened.")


