#Task 1
print("----Task 1-----")
subject = ["Operating Systems", "Algorithums" , "Computer Networks", "Auotmata", "Numerical"]
intro = ["Ahmed Baig", "20i-1884" , 2.2 , subject]
print(intro[0])
print(intro[3][0:2])

#Task 2
print("----Task 2-----")
def avglist(numbers):
        average = sum(numbers) / len(numbers)
        return average

numbers = [1,2,3,4,5,6,7,8,9,10]
avg = avglist(numbers)

if avg > 50:
    print(sum(numbers))
else:
    product = 1
    for number in numbers:
        product *= number
    print(product)

#Task 3
print("----Task 3-----")
class Bank_Account:
    def __init__(self):
        self.balance=0
        
    def Deposit(self):
        amount = float(input("Please enter the amount to be deposited: "))
        self.balance += amount
        print("Deposited Amount: ",amount)

    def Withdraw(self):
        amount = float(input("Please enter the amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn Amount: ", amount)
        else:
            print("Insufficient Balance")

    def Display(self):
        print("\nBalance: ",self.balance)


b = Bank_Account()
b.Deposit()
b.Withdraw()
b.Display()