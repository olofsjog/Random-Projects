tasklist = list()

while True:
    select0_list = [1, 2, 3, 4, 5, "Q", "q"]
    selectq_list = ["Q", "q"]
    selectm_list = ["M", "m"]
    select2_list = ["A,", "a"]
    select3_list = ["R,", "r"]
    
    listlength = len(tasklist)
    listlength_str = str(listlength)
    taskamount = " "

    if listlength > 0:
        taskamount = "(You Currenctly Have " + listlength_str + " Tasks)"

    else:
        taskamount = "(You Currenctly Have No Tasks)"
    

    print("MENU OF TASKLIST " + taskamount)
    print("-------------------")
    print("1. View Tasks   [1]")
    print("2. Add Tasks    [2]")
    print("3. Remove Tasks [3]")
    print("4. Mark Tasks   [4]")
    print("5. Sort Tasks   [5]")
    print("6. Quit         [Q]")
    print("-------------------")

    select0 = input("Select: ")

    if select0 == "1":
        print("\n\n\n\n\n\n\n\n\n\n")
        print("TASKLIST")
        print("-------------------")

        if listlength > 0:
            for index, task in enumerate(tasklist, start=1): 
                print(f"{index}. {task}")

        else:
            print("No Tasks Added")

        print("-------------------")

        select1 = 0

        while select1 not in selectq_list and select1 not in selectm_list:

            select1 = input("Select [M] for Menu or [Q] for Quit: ")

            if select1 in selectm_list:
                pass

            elif select1 in selectq_list:
                quit()

            else:
                print("\nInvalid Answer\n")

    elif select0 == "2":
        print("\n\n\n")
        print("ADD TASKS " + taskamount)
        print("-------------------")

        if listlength > 0:
            for index, task in enumerate(tasklist, start=1): 
                print(f"{index}. {task}")

        else:
            print("No Tasks Added")

        print("-------------------")

        select2 = 0

        while select2 not in selectq_list and select2 not in selectm_list and select2 not in select2_list:

            select2 = input("Select [M] for Menu, [Q] for Quit and [A] for Add: ")

            if select2 in selectm_list:
                pass

            elif select2 in selectq_list:
                quit()

            elif select2 in select2_list:
                print("\n\n\n\n\n\n\n\n\n\n")
                tasklist.append(input("Add Task:\n"))

            else:
                print("\nInvalid Answer\n")

    elif select0 == "3":
        print("\n\n\n")
        print("REMOVE TASKS " + taskamount)
        print("-------------------")

        if listlength > 0:
            for index, task in enumerate(tasklist, start=1): 
                print(f"{index}. {task}")

        else:
            print("No Tasks Added")

        print("-------------------")

        select3 = 0

        while select3 not in selectq_list and select3 not in selectm_list and select3 not in select3_list:

            select3 = input("Select [M] for Menu, [Q] for Quit and [R] for Remove: ")

            if select3 in selectm_list:
                pass

            elif select3 in selectq_list:
                quit()

            elif select3 in select3_list:
                print("\n\n\n\n\n\n\n\n\n\n")
                try:
                    tasklist.remove(input("Remove Task:\n"))
                except:
                    print("\nTry again.\n")
                    try:
                        remove = int(input("Remove Task:\n"))

                        if 0 <= remove < len(tasklist):
                            removed_task = tasklist.pop(remove)
                            print(f"Removed Task: {removed_task}")
                        else:
                            print("Invalid Task")

                    except:
                        print("ERROR!")
                        quit()

                print(tasklist)

            else:
                print("\nInvalid Answer\n")

    elif select0 in select0_list:
        quit()

    else:
        print("Invalid Selection")