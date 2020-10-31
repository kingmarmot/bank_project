# import uuid


class Acct:
    def __init__(self, balance=0):
        self.balance = balance

    def yield_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited {} dollars.".format(amount))

    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn {} dollars.".format(amount))


if __name__ == '__main__':
    selection_txt = """What would you like to do today? 
        [O]pen an account.
        [C]heck balance.
        [D]eposit funds.
        [W]ithdraw funds.
        [L]eave.\n"""
    overdraw_txt = "Sorry, that request cannot be processed. Requested amount exceeds balance."
    leave_txt = "Goodbye!"
    selection_val = ""

    print("Welcome to our bank!")

    my_acct = Acct()

    while True:
        selection_val = input(selection_txt)

        if selection_val == "O":
            print("Thank you for your business!")
            deposit_val = int(input("How much would you like to deposit? Please enter value: "))
            my_acct.deposit(deposit_val)

        elif selection_val == "C":
            print("Your balance is: {}".format(my_acct.yield_balance()))

        elif selection_val == "D":
            deposit_val = int(input("How much would you like to deposit? Please enter value: "))
            my_acct.deposit(deposit_val)

        elif selection_val == "W":
            withdraw_val = int(input("How much would you like to withdraw? Please enter value: "))
            if withdraw_val > my_acct.yield_balance():
                print(overdraw_txt)
            else:
                my_acct.withdraw(withdraw_val)

        elif selection_val == "L":
            print(leave_txt)
            break

        else:
            print("I'm sorry, that is not a valid selection. Please try again.")
