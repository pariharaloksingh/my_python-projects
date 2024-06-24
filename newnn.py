class bankaccount:
    def __init__(self,account_number,holder_name,bank_balance=0):
        self.account_number=account_number
        self.holder_name=holder_name
        self.bank_balance=bank_balance
        
    def deposit(self,amount):
        self.bank_balance+=amount
        print(f"ammount of Rs {amount} is deposited in your account available balance is {self.bank_balance}")  
        
        
    def withdral(self,amount):
        if amount <= self.bank_balance:  
         self.bank_balance -= amount 
         print(f"amount of rs {amount} withdrak from your account available balance is {self.bank_balance} ")
        
        else:
            print(f" balance is insufficent to withdral money")
            
    def get_balance(self):
        print(f"current balace of account {self.account_number} is  Rs {self.bank_balance}")    
        
        
account1=bankaccount(1234356789,'gopal_singh')
account1.deposit(500)
account1.deposit(10000)
        
            
        
        
        