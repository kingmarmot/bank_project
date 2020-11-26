import uuid


class Acct:
    def __init__(self, acct_num, password, balance):
        self.acct_num = acct_num
        self.password = password
        self.balance = balance

    def yield_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited {} dollars.".format(amount))

    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn {} dollars.".format(amount))


def set_acct_number():
    new_uuid = uuid.uuid4()
    acct_num = str(new_uuid)
    print("Thank you for your business! Your account number is: {}".format(str(acct_num)))
    return acct_num


def set_password():
    password = input("Please choose a password for your account: \n")
    print('Thank you for creating your account!')
    return password


def set_initial_balance():
    try:
        balance = float(input("Please enter an initial deposit: \n"))
        print('Thank you for your deposit!')
        return balance
    except:
        print("Sorry, that is not a valid deposit value.")


def create_acct():
    acct_num = set_acct_number()
    password = set_password()
    balance = set_initial_balance()
    new_account = Acct(acct_num, password, balance)
    return new_account


def log_on():
    user_acct_num, user_password = input("""
    Please enter your account number followed by your password:\n""").split()

    for account in account_list:
        if account.acct_num == user_acct_num and account.password == user_password:
            print("Logged on!")
            return account
        else:
            print("Sorry, the account number or password you entered is incorrect.")

    return None


if __name__ == '__main__':
    account_list = []
    welcome_txt = """Welcome to our bank! What would you like to do today?
        [L]og on.
        [O]pen account.
        [E]xit.\n"""
    acct_selection_txt = """What would you like to do today? 
        [C]heck balance.
        [D]eposit funds.
        [W]ithdraw funds.
        [L]og off.\n"""
    overdraw_txt = "Sorry, that request cannot be processed. Requested amount exceeds balance."
    leave_txt = "Logging off and returning to Main Menu."
    welcome_selection_val = ""
    acct_selection_val = ""

    while True:
        welcome_selection_val = input(welcome_txt)

        if welcome_selection_val == "O":
            new_acct = create_acct()
            account_list.append(new_acct)
            print("Returning to Main Menu!\n")

        elif welcome_selection_val == "L":
            my_acct = log_on()

            if my_acct is not None:
                while True:
                    acct_selection_val = input(acct_selection_txt)

                    if acct_selection_val == "C":
                        print("Your balance is: {}".format(my_acct.yield_balance()))

                    elif acct_selection_val == "D":
                        try:
                            deposit_val = float(input("How much would you like to deposit? Please enter value: "))
                        except:
                            print("Sorry, that is not a valid deposit value.")
                            continue

                        if deposit_val <= 0:
                            print("Sorry, please deposit an amount greater than zero.")
                        else:
                            my_acct.deposit(deposit_val)

                    elif acct_selection_val == "W":
                        try:
                            withdraw_val = int(input("How much would you like to withdraw? Please enter value: "))
                        except:
                            print("Sorry, please enter a positive value to withdraw from your account.")
                            continue

                        if withdraw_val > my_acct.yield_balance():
                            print(overdraw_txt)
                        else:
                            my_acct.withdraw(withdraw_val)

                    elif acct_selection_val == "L":
                        print(leave_txt)
                        my_acct = None
                        break

                    else:
                        print("I'm sorry, that is not a valid selection. Please try again.")

            else:
                print("Sorry, the account number or password is invalid. Returning to Main Menu.")

        elif welcome_selection_val == "E":
            print("Thank you for your business! Please come again!")
            break

        else:
            print("I'm sorry, that is not a valid selection. Please try again.")
