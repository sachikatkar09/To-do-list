print("*" * 10 + " TO DO LIST " + "*" * 10)

def display_menu():
    print("Enter 1 to add a task")
    print("Enter 2 to view tasks")
    print("Enter 3 to remove a task")
    print("Enter 4 to exit")

def add(todo_list):
    item = input("Enter a tasks to add:")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list")

def view(todo_list):
    if not todo_list:
        print("Your to-do list is empty")
    else:
        print("\nYour to-do list:")
        for index, item in enumerate(todo_list,start=1):
            print(f"{index}.{item}")

def remove(todo_list):
    if not todo_list:
        print("Your to-do list is empty . There is nothing to remove")
    else:
        view(todo_list)
        try:
            item_index = int(input("Enter the no . of item to remove:"))-1
            removed_item = todo_list.pop(item_index)
            print(f"'{removed_item}' has been removed ")
        except(IndexError , ValueError):
            print("Invalid input. Enter valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice 1/2/3/4:")

        if choice == "1":
            add(todo_list)

        elif choice =="2":
            view(todo_list)

        elif choice =="3":
            remove(todo_list)

        elif choice =="4":
            print("Exiting the to-do list")
            break

        else:
            print("Invalid input")


if __name__ == "__main__":
    main()



         