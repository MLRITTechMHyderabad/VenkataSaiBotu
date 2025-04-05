#Insufficent funds error exception class
class InsufficientFundsError(Exception) :
    def __init__(self, msg):
        super().__init__(msg)
#BankAccount class
class BankAccount :
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount) :
        try :
            if amount <= 0 :
                raise ValueError("Negative numbers not allowed...!!!")
            elif self.balance < amount :
                raise InsufficientFundsError("Withdraw amount is greter than Available balance")
            else :
                self.balance -= amount
                return self.balance
            
        except (ValueError, InsufficientFundsError, Exception) as e :
            return e

account = BankAccount(100)
print(account.withdraw(150))  # Should raise InsufficientFundsError
print(account.withdraw(-10))  # Should raise ValueError
print(account.withdraw(10))
