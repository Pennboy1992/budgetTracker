from table import table


def update_budget(arr):
    new_dict = {}
    print(table(arr))
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item = list(filter(lambda x: x["Item"] == item_name, arr))[0]
    print(item)
    try:
        update_name = int(input("Would you like to update the name of this item?\n1. Yes\n2. No\nEnter Corresponding "
                                "Number: "))
        name = input("What would you like to change the name to?: ")
    except ValueError:
        print("Please enter a valid choice(1 or 2)")
        update_name = int(input("Would you like to update the name of this item?\n1. Yes\n2. No\nEnter Corresponding "
                                "Number: "))
        name = input("What would you like to change the name to?: ")

    if update_name == 1:
        new_dict['Item'] = name

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
        new_dict['Amount'] = item['Amount']
    else:
        new_dict['Amount'] = amount

    arr.remove(item)
    item.update(new_dict)
    arr.append(item)
    return arr
