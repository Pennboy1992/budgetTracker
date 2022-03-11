import pyexcel
import pyfiglet
from update import update_budget
from table import table


def main():
    budget = []
    welcome_text = pyfiglet.figlet_format("Budget Tracker", font="slant")
    print(welcome_text)
    while True:
        try:
            new_item = int(input("What would you like to do?: \n1. Enter a new item\n2. Update an item\n3. Remove an "
                                 "item \n4. Print Stats\n5. Quit\nEnter Corresponding Number: "))
        except ValueError:
            print("Please enter a valid choice (1 or 2)")
            new_item = int(input("What would you like to do?: \n1. Enter a new item\n 2. Update an item\n3. Remove an "
                                 "item \n4. Print Stats \n5. Quit\nEnter Corresponding Number: "))

        if new_item == 1:
            budget_item(budget)
        elif new_item == 2:
            update_budget(budget)
        elif new_item == 3:
            remove_item(budget)
        elif new_item == 4:
            stats(budget)
        else:
            print("Here are your current items: ")
            print(table(budget))
            try:
                save_file = int(input("Would you like to save this to an excel file?: \n1.Yes\n2.No\nEnter "
                                      "Corresponding Number: "))
            except ValueError:
                print("Please enter a valid choice (1 or 2)")
                save_file = int(input("Would you like to save this to an excel file?: \n1.Yes\n2.No\nEnter "
                                      "Corresponding Number: "))
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
    print("The file " + filename + ".xls has been created and should be in your local directory")


def remove_item(arr):
    print(table(arr))
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item = list(filter(lambda x: x["Item"] == item_name, arr))[0]
    print(item)
    arr.remove(item)
    print(table(arr))


def stats(arr):
    if len(arr) > 2:
        total_income = 0
        total_expenses = 0
        for item in arr:
            if item['Type'] == 'Income':
                total_income += item['Amount']
            else:
                total_expenses += item['Amount']

        amount_list_income = [item['Amount'] for item in arr if item['Type'] == 'Income']
        amount_list_expense = [item['Amount'] for item in arr if item['Type'] == 'Expense']

        highest_income = list(filter(lambda x: x['Amount'] == max(amount_list_income), arr))[0]
        highest_expense = list(filter(lambda x: x['Amount'] == max(amount_list_expense), arr))[0]

        print("These are your current items: \n")
        print(table(arr))

        print(f"Your total income this month is: ${total_income: .2f}.")
        print(f"Your total expenses this months is: ${total_expenses: .2f}.")
        print(
            f"Your highest source of income is your {highest_income['Item']} at ${highest_income['Amount']:.2f} per month.")
        print(
            f"Your highest expense is your {highest_expense['Item']} which is costing ${highest_expense['Amount']:.2f} "
            f"per month.")
    else:
        print("We do not have enough data at this time to show budget statistics at this time.\n\n")





if __name__ == '__main__':
    main()
