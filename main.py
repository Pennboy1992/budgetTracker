def main():
    budget = []
    print("Welcome to Budget Tracking with Roman")
    while True:
        try:
            new_item = int(input("Do you wish you enter a new item: \n1.Yes\n2.No\n"))
        except ValueError:
            print("Please enter a valid choice (1 or 2)")
            new_item = int(input("Do you wish you enter a new item: \n1.Yes\n2.No\n"))

        if new_item == 1:
            budget_item(budget)
        else:
            print("Here is your current items: ")
            print(budget)
            break


def budget_item(arr):
    print("Enter a new item you wish to be added to your budget.")
    item_name = input("Enter the name for your item: ")
    try:
        income_or_debit = int(input("Is this income or a debit:\n1.Income\n2.Debit\nEnter Corresponding Number: "))
    except ValueError:
        print("Please enter a valid choice (1 or 2)")
        income_or_debit = int(input("Is this income or a debit:\n1.Income\n2.Debit\nEnter Corresponding Number: "))

    print(item_name)
    print(income_or_debit)
    if income_or_debit == 1:
        pay = float(input("How much will you be making from this source of income this month: "))
    else:
        pay = float(input("How much is this expense costing you per month: "))
    arr.append({"item": item_name, "type": "Income" if income_or_debit == 1 else "Expense", "amount": round(pay, 2)})
    return arr


if __name__ == '__main__':
    main()
