from table import table

# Function to remove items from our budget list given the name of the item.
def remove_item(arr):
    print(table(arr))
    item_name = input("Which item would you like to update?(Enter the fullname of the item you wish to update): \n")
    item = list(filter(lambda x: x["Item"] == item_name, arr))[0]
    print(item)
    arr.remove(item)
    print(table(arr))
    return arr
