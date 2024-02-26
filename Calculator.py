def calculator():
    while True:
        try:
            num_1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
            break
        except ValueError:
            print("შეცდომა, თქვენ არ შეიყვანიათ რიცხვი")

    while True:
        try:
            num_2 = float(input("შეიყვნეთ მეორე რიცხვი: "))
            break
        except ValueError:
            print("შეცდომა, თქვენ არ შეიყვანიათ რიცხვი")

    while True:
        operation = input("აირჩიეთ შემდეგი მათემატიკური ოპერაციიდან ერთ-ერთი +, -, *, /: ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("შეცდომა, არასწორი ოპერაცია. გთხოვთ შეიყვანოთ სწორი ოპერაცია.")

    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        if num_2 == 0:
            print("შეცდომა: ნულზე გაყოფა არ შეიძლება.")
            return
        else:
            result = num_1 / num_2

    print("შედეგი:", result)

calculator()