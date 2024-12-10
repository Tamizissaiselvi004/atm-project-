class Bank:
    def _init_(self):
        self.closingBal = 0  # Initialize balance to 0

    def display(self):
        print("Enter your options: ")
        print("1 for deposit")
        print("2 for withdraw")
        
        getOption = input()  # Get input from user
        
        if getOption == "1":
            self.deposit()  # Calls the deposit method
        elif getOption == "2":
            self.withdraw()  # Calls the withdraw method
        elif getOption!=1 or getOption!=2:
            print("Thanks")
            return  # Exit if invalid option is entered
        
        print("Your closing balance is:", self.closingBal)
        print("Do you want to continue:")
        a = input()
        if a == "Y" or a=='y':
            self.display()  # Recursively call display again
        else:
            print("Thanks for visiting our bank!")  # Exit message

    def deposit(self):
        depositAmount = int(input("Enter your deposit amount: "))  # Input for deposit amount
        self.closingBal=self.closingBal+depositAmount  # Add deposit amount to balance
        return self.closingBal

    def withdraw(self):
        withdrawAmount = int(input("Enter your withdraw amount: "))  # Input for withdraw amount
        if self.closingBal >= withdrawAmount:  # Check if there is enough balance
            self.closingBal = withdrawAmount  # Deduct from balance
            print("After withdrawal, your balance is:", self.closingBal)
        else:
            print(" No sufficient balance.")  # Error if not enough balance
            return self.closingBal


# Create a Bank object
bankobj = Bank()
bankobj.display()  # Start the program by calling the display method