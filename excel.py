import pyexcel
from table import table


def save_excel_file(arr):
    filename = input("\nWhat is the name of the *.xls file? ")
    pyexcel.save_as(records=arr, dest_file_name=f'{filename}.xls')
    print("The file " + filename + ".xls has been created and should be in your local directory")

def import_excel(arr):
    filename = input("\nWhat is the name of the *.xls file? ")
    items = pyexcel.get_records(file_name=f"{filename}.xls")
    for item in items:
        arr.append(item)
    print("Your items have successfully been imported.")
    print(table(arr))
    return arr

