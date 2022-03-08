import pyexcel


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
    arr.append({"Item": item_name, "Type": "Income" if income_or_debit == 1 else "Expense", "Amount": round(pay, 2)})
    return arr


def save_excel_file(arr):
    filename = input("\nWhat is the name of the *.xls file? ")
    pyexcel.save_as(records=arr, dest_file_name=f'{filename}.xls')
    print("The file " + filename + ".xls should be in your local directory")

def update_budget(arr,):
    for item in arr:
        print(item)
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item = filter(lambda x: x["Item"] == item_name, arr)



if __name__ == '__main__':
    main()
