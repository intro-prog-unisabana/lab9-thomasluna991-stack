from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    person = Person(name)

    while True:
        account_number = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))

        account = BankAccount(account_number, balance)
        person.add_account(account)

        done = input("Are you done adding accounts? (yes/no):\n")
        if done.lower() == "yes":
            break

    return person


def balance_summary(person_list):
    for person in person_list:
        total = 0
        for account in person.accounts:
            total += account.balance
        print(f"{person.name} : {total:.2f}")