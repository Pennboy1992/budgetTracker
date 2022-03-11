from table import table

# Function that is able to update every attribute of an entry in the budget tracker
def update_budget(arr):
    new_dict = {}
    print(table(arr))
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item_to_print = list(filter(lambda x: x["Item"] == item_name, arr))
    item = list(filter(lambda x: x["Item"] == item_name, arr))[0]
    print(table(item_to_print))
    try:
        update_name = int(input("Would you like to update the name of this item?\n1. Yes\n2. No\nEnter Corresponding "
                                "Number: "))

    except ValueError:
        print("Please enter a valid choice(1 or 2)")
        update_name = int(input("Would you like to update the name of this item?\n1. Yes\n2. No\nEnter Corresponding "
                                "Number: "))
        name = input("What would you like to change the name to?: ")

    if update_name == 1:
        name = input("What would you like to change the name to?: ")
        new_dict['Item'] = name
    else:
        new_dict['Item'] = item['Item']

    try:
        update_type = int(input("Will this be an income or an expense now?:\n1. Income\n2. Expense\nEnter "
                                "Corresponding Number: "))
    except ValueError:
        print("Please enter a valid choice(1 or 2)")
        update_type = int(input("Will this be an income or an expense now?:\n1. Income\n2. Expense\nEnter "
                                "Corresponding Number: "))

    if update_type == 1:
        new_dict['Type'] = 'Income'
    else:
        new_dict['Type'] = 'Expense'

    amount = float(input("What is the new amount for this item(if no changes enter 0): "))

    if amount == 0:
        new_dict['Amount'] = round(item['Amount'], 2)
    else:
        new_dict['Amount'] = round(amount, 2)

    arr.remove(item)
    item.update(new_dict)
    arr.append(item)
    return arr
