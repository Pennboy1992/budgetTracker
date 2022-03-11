from table import table

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

        print(f"Your total income this month is: ${total_income:.2f}.")
        print(f"Your total expenses this months is: ${total_expenses:.2f}.")
        print(
            f"Your highest source of income is your {highest_income['Item']} at ${highest_income['Amount']:.2f} per "
            f"month.")
        print(
            f"Your highest expense is your {highest_expense['Item']} which is costing ${highest_expense['Amount']:.2f} "
            f"per month.")
    else:
        print("We do not have enough data at this time to show budget statistics.\n")
