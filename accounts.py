import datetime                                                        # Importing datetime to calculate card expiry date
import random                                                          # Importing random to generate card number



class BasicAccount():
    """Basic Account does not have Overdraft"""

    #Initialize the account number to 0.
    accNumCount = 0


    #Initializer
    def __init__(self, acName, openingBalance):

        self.name = str(acName)
        self.balance = float(openingBalance)
        
        BasicAccount.accNumCount += 1                                   # Increment accNumCount by 1 each time a new account is added
        self.accNumCount = BasicAccount.accNumCount                     # Set the current instance of accNumCount to the account number 
        self.accNum = str(self.accNumCount)                             # Set accNum to ouput string of account number
        
        self.creationDate = datetime.datetime.now()                     # Datetime module to set the account creation date and to calculate cardExp


    #Default string
    def __str__(self):
        return "Account Name: {self.name}\n Account Balance: £{self.balance}".format(self=self)


    #Deposit method
    def deposit(self, newAmount):                                        # newAmount is the amount to be deposited
        if newAmount <= 0:                                               # Deposit conditions
            print("You can only deposit a positive amount of money!")   
            return
        else:
            self.balance += newAmount                                    # Add newAmount to balance


    #Withdraw method
    def withdraw(self, theAmount):                                       # theAmount = amount to be withdrawn
        self.amount = theAmount                                             

        if self.amount > self.balance:                                   # Cannot withdraw if amount requested is greater than balance
            print("Can not withdraw £{self.amount}".format(self=self))
        
        else:
            self.balance -= self.amount                                  # Decrease balance by the amount withdrawn
            
            print("{self.name} has withdrawn £{self.amount}. New balance is £{self.balance}".format(self=self))      
        
        
    #Get available balance method
    def getAvailableBalance(self):
        return (self.balance)                                             


    #Get balance method
    def getBalance(self):
        return (self.balance)


    #Print the balance
    def printBalance(self):
        print("£{self.balance}".format(self=self))
        

    #Get the account holder's name
    def getName(self):
       return (self.name)


    #Get the account numbers
    def getAcNum(self):
        return (self.accNum)


    #Issue new card method
    def issueNewCard(self): 
        cardNum = ""
        cardNumGen = []                                                    # Create an empty list to store card numbers 
        for j in range(16):                                                # Loop to get 16 random numbers
            num = random.randint(0,9)                                      # Card number should be between 0 and 9
            cardNumGen.append(num)                                         # Append card number generated to cardNum list
        cardNum = "".join(str(x) for x in cardNumGen)                      # Convert the card number list to a string 
        
        cardExpCalc = self.creationDate + datetime.timedelta(days = 1095)  # Calculate card expiry date 3 years (1095 days) from account creation date
        month = cardExpCalc.strftime("%m")                                 # Get the month value
        year = cardExpCalc.strftime("%y")                                  # Get the year value
        self.cardExp = (int(month), int(year))                             # Set cardExp in required format (mm, yy)
        return (self.cardExp)


    #Close account method
    def closeAccount(self):
        if self.balance < 0:                            
            print("Can not close account due to customer being overdrawn by £{-self.balace}".format(self=self))
            return False
        else:
            self.balance -= self.balance                                   # Make balance zero after closing account
            return True





class PremiumAccount(BasicAccount):
    """Premium Account is a Basic Account with Overdraft"""


    #Initializer
    def __init__(self, acName, openingBalance, initialOverdraft):
        super().__init__(acName, openingBalance)
        self.overdraftLimit = float(initialOverdraft)                      # Set initial overdraft limit
        print("A new Premium Account has been created. Welcome {self.name}! Your overdraft limit is £{self.overdraftLimit}".format(self=self))
        self.overdraftChange = self.overdraftLimit
        self.overdraft = True                                              


    #Withdrawal method of Premium account class
    def withdraw(self, theAmount):
        self.amount = theAmount
        try:
            if self.amount < 0.0 or self.amount > self.balance + self.overdraftLimit:               # Check if withdrawal amount is either less than zero (invalid) or greater than balance + overdraft
                raise ValueError
        except ValueError:
            print("Cannot withdraw £{self.amount}".format(self=self))
        
        else:
            self.balance -= self.amount                                                             # Decrease balance by the amount withdrawn 
            print("{self.name} has withdrawn £{self.amount}. New balance is £{self.balance}".format(self=self))

                
                   
    #Get balance method
    def getBalance(self):
        return float(self.balance)


    #Set new overdraft limit
    def setOverdraftLimit(self, newLimit):
        self.overdraftLimit = newLimit                                     # Set overdraft limit as newLimit
        return float(self.overdraftLimit)


    #Get the available balance including overdraft
    def getAvailableBalance(self):
        self.totalBalance1 = (self.balance + self.overdraftChange)         # Return available balance including overdraft
        return float(self.totalBalance1)


    #Print balance including overdraft
    def printBalance(self):
        self.combinedBalance = (self.balance + self.overdraftChange)       # Print available balance including overdraft
        print("£{self.combinedBalance}".format(self=self))


    #Close account method
    def closeAccount(self):
        if self.balance < 0:                     # Check if balance is not negative
            print("Can not close account due to customer being overdrawn by £{self.balance}".format(self=self))
            return False
        else:
            PremiumAccount.withdraw              # If balance is positive, call withdraw method
            return True