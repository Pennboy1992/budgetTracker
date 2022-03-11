from tabulate import tabulate

# Function that uses tabulate library to make more readable tables for the user
def table(arr_to_table):
    table_arr = []
    for items in arr_to_table:
        table_arr.append([items['Item'], items['Type'], items['Amount']])

    headers = ["Source", "Type", "Amount"]
    return tabulate(table_arr, headers, tablefmt="pretty")