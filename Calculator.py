def calculator():
    while True:
        try:
            num_1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
            num_2 = float(input("შეიყვნეთ მეორე რიცხვი: "))
            operation = input("აირჩიეთ შემდეგი მათემატიკური ოპერაციიდან ერთ-ერთი +, -, *, /: ")

            if operation == '+':
                result = num_1 + num_2
            elif operation == '-':
                result = num_1 - num_2
            elif operation == '*':
                result = num_1 * num_2
            elif operation == '/':
                if num_2 == 0:
                    print("ნულზე გაყოფის ერორი")
                    continue
                else:
                    result = num_1 / num_2
            else:
                print("მათემატიკური ოპერაცია არასწორია")
                continue

            print("შედეგი:", result)
            break

        except ValueError:
            print("შეცდომა, გთხოვთ შეიყვანოთ რიცხვი.")
    

calculator()

