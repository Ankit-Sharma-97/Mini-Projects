class atm(object):
    def __init__(self):
        self.balance=0
        self.pin=""
        self.menu()
    def menu(self):
        print("1. create pin \n2. deposit \n3. withdraw \n4. check balance \n5. exit")
        while(True):
            choise=int(input("enter choise"))
            if choise==1:
                self.create_pin()
            elif choise==2:
                self.deposit()
            elif choise==3:
                self.withdraw()
            elif choise==4:
                self.check_balance()
            else:
                exit()
    def create_pin(self):
        self.pin=int(input("enter your pin"))
        #return self.pin
    def deposit(self):
        temp=int(input("enter pin"))
        if self.pin == temp:
            balance=int(input("enter amount"))
            self.balance=self.balance+balance
            print("deposit")
        else:
            print("incorrect pin")
    def withdraw(self):
        temp=int(input("enter pin"))
        if temp==self.pin:
            deduct=int(input())
            self.balance=self.balance-deduct
        else:
            print("incorrect pin")
    def check_balance(self):
        print(self.balance)

    
    

a=atm()
