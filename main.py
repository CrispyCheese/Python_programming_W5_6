def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice():
    choice = input("Your choice: ").strip()
    if choice.isnumeric():
        return int(choice)
    else:
        return -1
    
def main():
    count = 0
    print("Program starting.")

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print(f"Count increased!")
        elif choice == 3:
            count = 0
            print("Cleared count!\n")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")

if __name__ == "__main__" or "unittest" in __import__("sys").modules:
    main()
