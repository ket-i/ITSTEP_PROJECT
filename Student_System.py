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
                   print("სტუდენტი ვერ დაემატა, სტუდენტის სახელი უნდა შეიცავდეს მხოლოდ ასოებს, სცადე თავიდან.")
                   break
                elif not roll_number.isdigit():
                   print("სტუდენტი ვერ დაემატა, სიის ნომერი უნდა იყოს მხოლოდ ციფრები, სცადე თავიდან.")
                   break
                elif grade not in ['A', 'B', 'C', 'D']:
                    print("სტუდენტი ვერ დაემატა, შეფასება უნდა იყოს 'A', 'B', 'C' ან 'D', სცადე თავიდან.")
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
            print("სისტემაში არ არის სტუდენტები.")
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
            print("აღნიშნული ნომრით სიაში არ არის სტუდენტი.")

    def update_student_grade(self, roll_number, new_grade):
        for student in self.students:
            if student.roll_number == roll_number:
                student.grade = new_grade
                print("სტუდენტის შეფასება განახლდა")
                break
        else:
            print("არ არის სტუდენტი.")
    def save_results(self, filename):
        with open(filename, 'w') as file:
            if not self.students:
                file.write("სისტემაში არ იძბნება სტუდენტი.")
            else:
                file.write("სტუდენტების სია:\n")
                for student in self.students:
                    file.write(f"სახელი: {student.name}, სიის ნომერი: {student.roll_number}, შეფასება: {student.grade}\n")
def main():
    sms = StudentManagementSystem()

    while True:
        print("\nMenu:")
        print("1. ახალი სტუდენტის დამატება")
        print("2. ყველა სტუდენტის ნახვა")
        print("3. სტუდენტის ძებნა სიის ნომერის მიხედვით")
        print("4. სტუდენტის შეფასების განახლება")
        print("5. შეფასების შენახვა ფაილში")
        print("6. გასვლა")

        choice = input("მენიუდან აირჩიე ნომერი რა ოპერაცია გინდა განახორციელო: ")

        if not choice.isdigit() or not 0 <= int(choice) <= 6:
            print("შეცდომა: შეიყვანეთ რიცხვი 0-დან 6-მდე.")
            continue

        choice = int(choice)

        if choice == 1:
            # Your existing code for adding a student
        elif choice == 2:
            print("ყველა სტუდენტის ნახვა:")
            sms.view_all_students()
        elif choice == 3:
            # Your existing code for searching for a student
        elif choice == 4:
            # Your existing code for updating a student's grade
        elif choice == 5:
            filename = input("შეიყვანე ფაილის სახელი: ")
            sms.save_results(filename)
            print("შეფასებები შენახულია ფაილში.")
        elif choice == 6:
            print("პროგრამიდან გამოსვლა")
            break
        else:
            print("შეცდომა, გთხოვთ აირჩიოთ ოპერაციის ნომერი თავიდან")


main()