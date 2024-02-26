class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_number, grade):
        while True:
            try:
                if not name.isalpha():
                   print("სტუდენტი ვერ დაემატა, სტუდენტის სახელი არ უნდა შეიცავდეს რიცხვს, სცადე თავიდან.")
                   break
                elif not roll_number.isdigit():
                   print("სტუდენტი ვერ დაემატა, სიის ნომერი უნდა იყოს რიცხვი, სცადე თავიდან.")
                   break
                elif not grade.isalpha():
                    print("სტუდენტი ვერ დაემატა, ქულა შეიძლება იყოს 'A', 'B', 'C', or 'D', სცადე თავიდან .")
                    break
                else:
                    student = Student(name, roll_number, grade)
                    self.students.append(student)
                    print("სტუდენტი წარმატებით დაემატა")
                break  
            except ValueError:
                print("შეცდომა")
                break

    def view_all_students(self):
        if not self.students:
            print("სისტემაში არ იძბნება სტუდენტი.")
        else:
            print("სტუდენტების სია:")
            for student in self.students:
                print(f"სახელი: {student.name}, სიის ნომერი: {student.roll_number}, შეფასება: {student.grade}")

    def search_student_by_roll_number(self, roll_number):
        found = False
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"ნაპოვნის სტუდენტის სახელი: {student.name}, სიის ნომერი: {student.roll_number}, შეფასება: {student.grade}")
                found = True
                break
        if not found:
            print("აღნიშნული ნომრით სიაში არ იძებნება სტუდენტი.")

    def update_student_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("დაემატა სტუდენტის ქულა")
                break
        else:
            print("არ იძებნება სტუდენტი.")


def main():
    sms = StudentManagementSystem()


    while True:
        print("\nMenu:")
        print("1. ახალი სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის ძებნა სიის ნომერის მიხედვით")
        print("4. სტუდენტის შეფასების განახლება")
        print("5. გასვლა")

        choice = input("მენიუდან აირჩიე ნომერი რა ოპერაცია გინდა განახორციელო: ")

        if not choice.isdigit() or not 0 <= int(choice) <= 5:
            print("შეცდომა: შეიყვანეთ რიცხვი 0-დან 5-მდე.")
            continue

        choice = int(choice)

        if choice == 1:
            name = input("შეიყვანე სტუდენტის სახელი: ")
            roll_number = input("შეიყვანე სტუდენტის სიის ნომერი: ")
            grade = input("შეიყვანე სტუდენტის შეფასება: ")
            sms.add_student(name, roll_number, grade)
        elif choice == 2:
            print("ყველა სტუდენტის ნახვა:")
            sms.view_all_students()
        elif choice == 3:
            roll_number = input("შეიყვანე სტუდენტის სიის ნომერი ")
            sms.search_student_by_roll_number(roll_number)
        elif choice == 4:
            roll_number = input("სტუდენტის შეფასების გასაახელბლად შეიყვანე სტუდენტის ნომერი: ")
            new_grade = input("შეიყვანე ახალი შეფასება: ")
            sms.update_student_grade(roll_number, new_grade)
        elif choice == 5:
            print("პროგრამიდან გამოსვლა")
            break
        else:
            print("შეცდომა, გთხოვთ აირჩიოთ ოპერაციის ნომერი თავიდან")


main()


