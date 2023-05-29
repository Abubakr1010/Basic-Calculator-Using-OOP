from functions import Rules


# Used OOP in order that i can also practice it and created a Class called Rules

while True:
    # user is asked to input a number
    user_input = input("write your first number \n")
    user_input = user_input.strip().split("  ")
    print(user_input)

    # input numbers are converted into integers
    user_number_1 = int(user_input[0])
    user_number_2 = int(user_input[2])
    decision = user_input[1]

    cal = Rules(user_number_1, user_number_2)
    result = cal.operations(decision)
    print(result)

    break






