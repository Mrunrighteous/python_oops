from bank_accounts import *

Peter = BankAccount(1000, "Peter")
Tony = BankAccount(100000000, "Tony")

Peter.get_balance()
Tony.get_balance()

Peter.deposit(500)

Peter.withdraw(1000000)
Tony.withdraw(10)

Tony.transfer(10000, Peter)


Steve = InterestRewardsAcc(100000, "Steve")
Steve.get_balance()
Steve.deposit(100)
Steve.transfer(100, Peter)

Strange = SavingsAcc(10000, "Strange")
Strange.get_balance()
Strange.deposit(1000)
Strange.transfer(100, Peter)
