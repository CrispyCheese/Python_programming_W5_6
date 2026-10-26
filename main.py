def showOptions ():
    print ("Options:\n1 - Show count\n2 - Increase count\n3 - Reset count\n0 - Exit")
    return None

def askChoice() -> int:
    choice = input("Your choice: ")
    if (choice.isnumeric() != True):
        return 4
    else:
        return int(choice)
    
def main():
    print ("Program starting.")
    counter = 0
    while True:
        showOptions ()
        userChoice = askChoice ()
        if (userChoice == 0):
            print ("Exiting program.\n")
            break
        elif (userChoice == 1):
            print (f"Current count - {counter}\n")
        elif (userChoice == 2):
            counter += 1
            print ("Count increased!\n")
        elif (userChoice == 3):
            counter = 0
            print ("Cleared count!\n")
        else:
            print ("Unknown option!\n")
    print ("Program ending.")
main()
