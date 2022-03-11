from stats import stats
from update import update_budget
from new_item import budget_item
from excel import *
from remove import remove_item
import pyfiglet

# Main function of the program that leads to all other functions into the program
def budget():
    budget_arr = []
    welcome_text = pyfiglet.figlet_format("Budget Tracker", font="slant")
    print(welcome_text)
    while True:
        try:
            new_item = int(input("What would you like to do?: \n1. Enter a new item\n2. Update an item\n3. Remove an "
                                 "item \n4. Print Stats\n5. Import Excel File\n6. Quit\nEnter Corresponding Number: "))
        except ValueError:
            print("Please enter a valid choice (1 or 2)")
            new_item = int(input("What would you like to do?: \n1. Enter a new item\n 2. Update an item\n3. Remove an "
                                 "item \n4. Print Stats \n5. Import Excel File\n6. Quit\nEnter Corresponding Number: "))

        if new_item == 1:
            budget_item(budget_arr)
        elif new_item == 2:
            update_budget(budget_arr)
        elif new_item == 3:
            remove_item(budget_arr)
        elif new_item == 4:
            stats(budget_arr)
        elif new_item == 5:
            import_excel(budget_arr)
        else:
            print("Here are your current items: ")
            print(table(budget_arr))
            try:
                save_file = int(input("Would you like to save this to an excel file?: \n1.Yes\n2.No\nEnter "
                                      "Corresponding Number: "))
            except ValueError:
                print("Please enter a valid choice (1 or 2)")
                save_file = int(input("Would you like to save this to an excel file?: \n1.Yes\n2.No\nEnter "
                                      "Corresponding Number: "))
            if save_file == 1:
                save_excel_file(budget_arr)
                print("Thank you for using our Budget Tracker")
                break
            else:
                print("Thank you for using our Budget Tracker")
                break
