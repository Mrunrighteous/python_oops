class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accountName):
        self.balance = initialAmount
        self.name = accountName
        print(f"\nAccount '{self.name}' created\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("Deposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWidthdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nwidthdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete.\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted {error}")


class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print("\nDeposit complete.")
        self.get_balance()


class SavingsAcc(InterestRewardsAcc):
    def __init__(self, initalAmount, accountName):
        super().__init__(initalAmount, accountName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWidthdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWidthdraw interrupted {error}")
