#pillars of oops: polymorphism, abtraction, encapsulation and inheritance

#abstraction: hiding the implementation details of a class and showing only the result
#encapsulation: wrapping data and functions in a single unit/object/capsule



class Car:
    color="Red"
    brand="mercedes"

    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.brk=False
        self.clutch=True
        print("car started")


car1=Car()
print(car1.color)   
print(car1.brand) 
car1.start()



class Bank:
    def __init__(self, accno, balance):
        self.accno=accno
        self.balance=balance
        print("bank account is created for this user")

    def debit(self, amount):
        self.balance -= amount
        print("account debited = ", self.balance)

    def credit(self, amount):
        self.balance += amount
        print("account credited = ",self.balance)            
   
    def get_balance(self):
        return self.balance

acc1=Bank(123, 10000)
print(acc1.balance)
print(acc1.accno)
acc1.debit(1000)
acc1.credit(101)

