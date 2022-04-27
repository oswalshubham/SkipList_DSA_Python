import SkipList


def getOptions():
    print("Enter one of the following options:")
    print("1. Insert, 2. Delete, 3. Find, 4. Closest key After, 5. Display, 6. Exit")
    print("")

    choice = input("Enter your choice:")
    if not choice.isdigit() or int(choice)<1 or int(choice)>6:
        print("Please enter valid choice from 1-6.")
        return None
    else:
        return int(choice)



option = True
skipList = SkipList.SkipList()
while option:
    choice = getOptions()
    if choice == None:
        continue

    else:
        if choice == 1:
            key = int(input("Enter key of the node : "))
            value = int(input("Enter the value : "))
            skipList.insertElement(key, value)
            print(skipList.display())

        elif choice == 2:
            key = int(input("Enter key of the node to delete : "))

            skipList.removeElement(key)
            
            print(skipList.display())

        elif choice == 3:
            key = int(input("Enter key to find : "))

            value = skipList.findElement(key)
            if value == None:
                print("Key not found in skipList.\n")
            else:
                print(f"Key found. Value of key {key} = {value}.\n")

        elif choice == 4:
            key = int(input("Enter key to find the nearest node after given key : "))
            closestkey = skipList.closestKeyAfter(key)
            print(f"Closest key after {key} is : {closestkey}\n\n")

        elif choice == 5:
            print(skipList.display())

        else:
            option = False



