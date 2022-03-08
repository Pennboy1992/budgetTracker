import pyexcel


def main():
    budget = []
    print("Welcome to Budget Tracking with Roman")
    while True:
        try:
            new_item = int(input("What would you like to do?: \n1. Enter a new item\n2. Update an item\n3. Remove an "
                                 "item \n4. Print Stats\n5. Quit\n"))
        except ValueError:
            print("Please enter a valid choice (1 or 2)")
            new_item = int(input("What would you like to do?: \n1. Enter a new item\n 2. Update an item\n3. Remove an "
                                 "item \n4. Print Stats \n5. Quit"))

        if new_item == 1:
            budget_item(budget)
        elif new_item == 2:
            update_budget(budget)
        elif new_item == 3:
            remove_item(budget)
        elif new_item == 4:
            stats(budget)
        else:
            print("Here is your current items: ")
            print(budget)
            try:
                save_file = int(input("Would you like to save this to an excel file?: \n1.Yes\n2.No\n"))
            except ValueError:
                print("Please enter a valid choice (1 or 2)")
                save_file = int(input("Would you like to save this to an excel file?: \n1.Yes\n2.No\n"))
            if save_file == 1:
                save_excel_file(budget)
                print("Thank you for using our Budget Tracker")
                break
            else:
                print("Thank you for using our Budget Tracker")
                break


def budget_item(arr):
    print("Enter a new item you wish to be added to your budget.")
    item_name = input("Enter the name for your item: ")
    try:
        income_or_debit = int(input("Is this income or a debit:\n1.Income\n2.Expense\nEnter Corresponding Number: "))
    except ValueError:
        print("Please enter a valid choice (1 or 2)")
        income_or_debit = int(input("Is this income or a debit:\n1.Income\n2.Expense\nEnter Corresponding Number: "))

    print(item_name)
    print(income_or_debit)
    if income_or_debit == 1:
        pay = float(input("How much will you be making from this source of income this month: "))
    else:
        pay = float(input("How much is this expense costing you per month: "))
    arr.append({"Item": item_name, "Type": "Income" if income_or_debit == 1 else "Expense", "Amount": round(pay, 2)})
    return arr


def save_excel_file(arr):
    filename = input("\nWhat is the name of the *.xls file? ")
    pyexcel.save_as(records=arr, dest_file_name=f'{filename}.xls')
    print("The file " + filename + ".xls should be in your local directory")


def update_budget(arr):
    for item in arr:
        print(item)
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item = list(filter(lambda x: x["Item"] == item_name, arr))[0]
    print(item)
    arr.remove(item)
    print(arr)


def remove_item(arr):
    for item in arr:
        print(item)
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item = list(filter(lambda x: x["Item"] == item_name, arr))[0]
    print(item)
    arr.remove(item)
    print(arr)

def stats(arr):
    total_income = 0
    total_expenses = 0
    for item in arr:
        if item['Type'] == 'Income':
            total_income += item['Amount']
        else:
            total_expenses += item['Amount']

    print(f"Your total income this month is: {total_income: .2f}")
    print(f"Your total expenses this months is: {total_expenses: .2f}")


if __name__ == '__main__':
    main()
