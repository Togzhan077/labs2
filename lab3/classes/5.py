class BankAccount:
    def __init__(self, owner, balance=0):
        """Инициализация банковского счета с владельцем и начальным балансом."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Внесение депозита на счет."""
        if amount > 0:
            self.balance += amount
            print(f"На счет {self.owner} внесено {amount} единиц.")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        """Снятие средств со счета."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Со счета {self.owner} снято {amount} единиц.")
        else:
            print(f"Недостаточно средств для снятия {amount} единиц. Доступный баланс: {self.balance}.")

    def get_balance(self):
        """Получение текущего баланса счета."""
        return self.balance

# Пример использования
account = BankAccount("Иван Иванов", 1000)

# Внесение депозита
account.deposit(500)  # Ожидаемый вывод: На счет Иван Иванов внесено 500 единиц.

# Снятие средств
account.withdraw(200)  # Ожидаемый вывод: Со счета Иван Иванов снято 200 единиц.

# Попытка снять больше средств, чем доступно
account.withdraw(1500)  # Ожидаемый вывод: Недостаточно средств для снятия 1500 единиц. Доступный баланс: 1300.

# Получение текущего баланса
print(f"Текущий баланс: {account.get_balance()} единиц.")  # Ожидаемый вывод: Текущий баланс: 1300 единиц.
