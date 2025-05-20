class bank:
    def __init__(self, accountholder,balance=0):
        self.accountholder = accountholder
        self.balance = balance
    
    def deposit(self,amount):

        self.balance+=amount
        print(f"you have deposited {amount} in the bank. your new balance is{self.balance}")

    def withdrew(Self, amount):
        if amount> Self.balance:
            print("you dont have sufficient balance in the bank")
        else:       
            Self.balance-=amount
            print(f"yoou have withdrew {amount} from the bank")
    
   
    
    def display_info(self):
      print(f"the accountholder : {self.accountholder}")
      print(f"your current balance is: {self.balance}")
        

nicasia = bank("samyam maharjan")
nicasia.deposit(20000)
nicasia.withdrew(5000)
nicasia.display_info()
        