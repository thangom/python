#Project-two ATM System

class bank:
    def __init__(self, total, name):
        self.total = total
        self.name = name

    def display(self):        
        if acc_bank ==1 and upin ==1234:
            print("Account Holder Name: ", self.name)
            self.option()
        elif acc_bank ==2 and upin ==1111:
            print("Account Holder Name: ", self.name)
            self.option()
        else:
            print("Take your card and Try again!")
        
        
    def deposit(self):
        print("Your Total Balance: ", self.total)
        dep = int(input("How much amount to be deposit: "))
        self.total = self.total + dep
        print("Your new Balance: ", self.total)
        self.resume()

    def withdraw(self):
        print("Your Total Balance: ", self.total)
        wdr = int(input("How much amount to be withdraw: "))
        self.total = self.total - wdr
        if wdr <= self.total:
            print("Your new Balance: ", self.total)
        else:
            print("Insufficient amount to withdraw")
        self.resume()

    def loan_amount(self):
        loanamount = int(input("Enter your Loan amount: "))
        if acc_bank == 1:

            if loanamount <= 100000:
                print("Your Loan amount Interst is 3.7%")
                interest = (loanamount // 100) * 3.7
                print("Your Interst amount is ", interest)
            else:
                print("Your Loan amount Interst is 2.7%")
                interest = (loanamount // 100) * 2.7
                print("Your Interst amount is ", interest)
            self.resume()
        elif acc_bank==2:
            if loanamount <= 100000:
                print("Your Loan amount Interst is 4.7%")
                interest = (loanamount // 100) * 4.7
                print("Your Interst amount is ", interest)
            else:
                print("Your Loan amount Interst is 3.7%")
                interest = (loanamount // 100) * 3.7
                print("Your Interst amount is ", interest)
            self.resume()
    def option(self):
        choice = int(input("Enter your option: 1.deposit\t 2.withdrawal\t 3.Loan amount\n "))
        if choice == 1:
            self.deposit()
        elif choice == 2:
            self.withdraw()
        elif choice == 3:
            self.loan_amount()
        else:
            print("Invalid Option")
            self.resume()

    def resume(self):
        get2 = input("Are you continue?(y/n) ")
        if get2 == 'y':
            self.option()
        elif get2 == 'n':
            print("Thank you for using")
            
class sbi(bank):
    def __init__(self,total,upin,name):
        self.total=total
        self.upin=upin
        self.name=name
        if upin == 1234:
            super().__init__(total,name)
        else:
            print("You entered wrong pin")
            
class indian(bank):
    def __init__(self,total,upin,name):
        self.total=total
        self.upin=upin
        self.name=name
        if upin == 1111:
            super().__init__(total,name)
        else:
            print("You entered wrong pin")
            
if __name__=='__main__':
    acc_bank=int(input("Choose Your Bank: 1.SBI\t 2.Indian\n"))
    
    if acc_bank==1:
        upin = int(input("Enter ATM Pin: "))
        usr1=sbi(12000,upin,name="Thangam")
        usr1.display()
    elif acc_bank==2:
        upin = int(input("Enter ATM Pin: "))
        usr2=indian(13000,upin,name="Durai")
        usr2.display()
    else:
        print("You entered wrong option and Take out Your card")
