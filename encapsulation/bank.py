'''b) Suggest how the BankAccount class could use encapsulation to protect the balance. (2 marks) 
c) Explain one benefit of using encapsulation in this scenario. (2 marks) '''

class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.__balance = balance
    
