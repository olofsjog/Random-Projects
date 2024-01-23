while True:
    num1 = input("First Number: ")
    try:
        num1i = int(num1)
    except ValueError:
        print("Incorrect Number. Try Again.")
        continue

    num2 = input("Second Number: ")
    try:
        num2i = int(num2)
    except ValueError:
        print("Incorrect Number. Try Again.")
        continue

    method = input("Method: ")

    try:
        if method == '+':
            answer = num1i + num2i
        elif method == '-':
            answer = num1i - num2i
        else:
            print("Incorrect Method. Try Again. Else")
            continue

        answer_str = str(answer)
        maxlen = max(len(str(num1i)), len(str(num2i)), len(answer_str))+2

        arranged_problem = f"{str(num1i).rjust(maxlen-1)}\n{method} {str(num2i).rjust((maxlen-1)- len(method))}"

        anslen = maxlen - len(answer_str)

        ansspace = " " * anslen

        num1space = (maxlen - len(num1))-1

        print(' ' * num1space + arranged_problem)
        print('-' * maxlen)
        print(ansspace + str(answer))
        quit()
    except Exception as e:
        print(f"Error: {e}")
        continue
