import random

def vars():
    global battery, firstTime, userId, balance, budget, income, currency, password
    battery = True
    firstTime = True
    userId = None
    balance = 5000
    budget = 0
    income = 0
    currency = ""
    password = ""

def main():
    vars()
    while battery:
        if firstTime:
            first_Time()
        else:
            notFirstTime()
        exit_game = input("Do you want to (C)ontinue or (E)xit? ").upper()
        if exit_game == "E":
            break

def first_Time():
    global firstTime, userId, currency
    print("Hey, there, user")
    userId = input("Type your UserID: ")
    global password
    password = input(f"Type your password (for user {userId}): ")
    currency = input("In what currency is your bank account? ")
    print(f"As a signing bonus, you get 5000 {currency}")
    firstTime = False

def notFirstTime():
    print("Hey, there.")
    a = input("Type in your UserID: ")
    if a == userId:
        b = input("Type in your password: ")
        if b == password:
            print(f"Welcome back, {userId}")
            action = input("Would you like to (I)nvest or (T)ransfer? ").upper()
            if action == "I":
                invest()
            elif action == "T":
                transfer()
        else:
            print("Wrong password")

def invest():
    global balance
    try:
        a = int(input("How much do you want to invest? "))
        if a <= 0 or a > balance:
            raise ValueError("Invalid investment amount.")
        chance = random.randint(1, 100)
        percent = chance / 100
        tf = random.choice([True, False])
        if tf:
            balance -= a
            balance_stat()
            b = a * percent
            balance += b + a
            balance_stat()
        else:
            balance -= a
            balance_stat()
            b = a * percent
            balance -= b
            balance_stat()
    except ValueError as e:
        print(e)

def transfer():
    global balance, budget, income
    try:
        a = input("Which account has the money you want to transfer? (balance, budget, or income): ").lower()
        b = int(input("How much do you want to transfer? "))
        c = input("To which account do you want to transfer to? ").lower()

        if b <= 0:
            raise ValueError("Transfer amount must be positive.")

        if a not in ["balance", "budget", "income"] or c not in ["balance", "budget", "income"]:
            raise ValueError("Invalid account specified.")

        if a == "balance":
            balance -= b
            balance_stat()
        elif a == "budget":
            budget -= b
            budget_stat()
        elif a == "income":
            income -= b
            income_stat()

        if c == "balance":
            balance += b
            balance_stat()
        elif c == "budget":
            budget += b
            budget_stat()
        elif c == "income":
            income += b
            income_stat()
    except ValueError as e:
        print(e)

def balance_stat():
    print(f"Your balance has been updated to {balance} {currency}")

def budget_stat():
    print(f"Your budget has been updated to {budget} {currency}")

def income_stat():
    print(f"Your income has been updated to {income} {currency}")