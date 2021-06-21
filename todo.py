# simple python to-do app project
user_input = 'random'
# crete a list for items
data = list()


# we are going to create 4 options
# 1.Add an item
# 2.Mark as done
# 3.View items
# 4.exit

# lets  create menu items using function

def displayMenu():
    print("MENU")
    print("1.Add an item:")
    print("2.Mark as done:")
    print("3.View items:")
    print("4.exit:")


while user_input != '4':

    displayMenu()
    user_input = input("Enter your choice:")

    if user_input == '1':
        item = input("what is to be done?")
        data.append(item)
        print("added items are:" + item)
    elif user_input == '2':
        item = input("what is to be marked as done")
        # if item is present in data list then remove it from the list
        # else print does not exist in list
        if item in data:
            data.remove(item)
            print("removed items:" + item)
        else:
            print("item does not exist in the to-do list")
    elif user_input == '3':
        print("list of TO-DO items:")
        for items in data:
            print(item)

    elif user_input == '4':
        print("good bye")
