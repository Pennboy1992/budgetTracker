from tabulate import tabulate

def table(arr_to_table):
    table_arr = []
    for items in arr_to_table:
        table_arr.append([items['Item'], items['Type'], items['Amount']])

    headers = ["Source", "Type", "Amount"]
    return tabulate(table_arr, headers, tablefmt="pretty")