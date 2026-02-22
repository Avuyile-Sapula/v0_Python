class CreditCard:
    def __init__(self, name, number, bank="ABC Bank"):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0

    def change(self, amount):
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <=0):
            print("Change denied")
        else:
            self.balance += amount
        
    def pay(self, amount):
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <=0) or (amount > self.balance):
            print("Change denied")
        else:
            self.balance -= amount
    
    def __str__(self):
        info = f"Name: {self.name} \n Number: {self.number} \n Bank: {self.bank} \n Balance: {self.balance}"
        return info
    

u1 = CreditCard("Robert Welker", 123456789)
print(u1)

u1.change(2000)
print(u1)

u1.pay(500)
print(u1)

