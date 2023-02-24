# Bank-Accounts
Bank Accounts

In this program, two classes are implemented in Python: BasicAccount and PremiumAccount.

The classes are adherent to the following UML Class diagram:

![UML Diagram](https://github.com/kevin14fe/Bank-Accounts/blob/main/uml.png)

 
Variables:

The variables of the classes are described as follows:

    name – the account holder's name.

    acNum – the number of the account. This is “serial”, meaning that the first account to be created has number 1, the second account to be created has number 2, and so on.

    balance – The balance (in pounds) of the account.

    cardNum – The card number, which is a string containing a 16-digit number (the random module is imported for this).

    cardExp - a tuple, where the first element is an integer corresponding to the month and the second element is 2-digit year. Eg: 03/23 represents March 2023. (the datetime module is imported for this).

    overdraft – a Boolean variable, which is True if the account has an overdraft, and False if  does not.

    overdraftLimit – The amount that the account can go overdrawn by.

 

 

Methods:

The methods are as follows:

    __init__(self, str, float)

    Initialiser giving the account name and opening balance.

    __init__(self, str, float, float)
    initialiser giving the account name, opening balance, and overdraft limit (0 or above).

    deposit(self, float)
    Deposits the stated amount into the account, and adjusts the balance appropriately. Deposits must be a positive amount.

    withdraw(self, float)
    Withdraws the stated amount from the account, prints a message of “<Name> has withdrawn £<amount>. New balance is £<amount>”.
    If an invalid amount is requested, then the following message is printed, and the method then terminates: “Can not withdraw £<amount>".
    An amount is considered to be invalid if it is larger than the balance for (normal) accounts and if it is larger than the balance + overdraft limit for premium accounts.

    getAvailableBalance(self)
    Returns the total balance that is available in the account as a float. It takes into account any overdraft that is available.

    getBalance(self)
    returns the balance of the account as a float. If the account is overdrawn, then it returns a negative value.

    printBalance(self)
    prints to screen the balance of the account. If an overdraft is available, then this is also printed and it shows how much overdraft is remaining.

    getName(self)
    Returns the name of the account holder as a string.

    getAcNum(self)
    Returns the account number as a string.

    issueNewCard(self)
    Creates a new card number, with the expiry date being 3 years to the month from now (e.g., if today is 1/12/21, then the expiry date would be (12/24)).

    closeAccount(self)
    To be called before deleting of the object instance. Returns any balance to the customer (via the withdraw method) and returns True.
    Returns False if the customer is in debt to the bank, and prints message “Can not close account due to customer being overdrawn by £<amount>”.
    Clarification: The account instance is not actually deleted. This function will simply do the relevant "housekeeping" in the account, and return a Boolean value.

    setOverdraftLimit(self, float)
    Sets the overdraft limit to the stated amount

 

In addition to the above, suitable string representations are defined that give the account name, available balance, and overdraft details.
