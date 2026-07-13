import json

class Student:
    def __init__(self,name,roll,age,gpa):
        self.name = name
        self.roll = roll
        self.age = age
        self.gpa = gpa
    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll,
            "age": self.age,
            "gpa": self.gpa
        }


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.load_from_file()
        

    def add_student(self):
       name = input("Enter Student Name: ").capitalize
       roll = int(input("Enter Student Roll Number: "))
       age = int(input("Enter Student Age: "))
       gpa = float(input("Enter Student GPA: "))
   
       if gpa < 0 or gpa > 4:
           print("Invalid GPA! GPA must be between 0 and 4.")
           return
   
       for student in self.students:
           if student.roll == roll:
               print("Student with this roll number already exists.")
               return
   
       student = Student(name, roll, age, gpa)
       self.students.append(student)
       self.save_to_file()
   
       print("Student added successfully!")

    def display_students(self):
        if not self.students:
            print("No Students Availabe")
            return
        else:
            for student in self.students:
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll}")
                print(f"Age: {student.age}")
                print(f"GPA: {student.gpa}")
                print("-" * 30)

    def update_student(self):
        roll = int(input("Enter Student Roll Number: "))
        found = False
        for student in self.students:
            if student.roll == roll:
                found = True
                name = input("Enter New Name: ")
                age = int(input("Enter new Age: "))
                gpa = float(input("Enter new GPA: "))
                if gpa < 0 or gpa > 4:
                     print("Invalid GPA! GPA must be between 0 and 4.")
                     return
                student.name = name
                student.age = age
                student.gpa = gpa
                self.save_to_file()
                print("Student updated successfully!")
                break
                
        if not found:
            print("No student is Found")
    
                

    def search_student(self):
        search_roll = int(input("Enter Student Roll Number to search: "))
        found = False
        for student in self.students:    
            if student.roll == search_roll:
                found = True
                print("-" * 30)
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll}")
                print(f"Age: {student.age}")
                print(f"GPA: {student.gpa}")
                break
                
        if not found:
            print("No student is Found")
        
                

    def delete_student(self):
        roll = int(input("Enter Student Roll Number to search: "))
        found = False
        for student in self.students:    
            if student.roll == roll:
                found = True
                print(f"{student.roll} Deleted Successfully")
                self.students.remove(student)
                self.save_to_file()
                break
            
        if not found:
            print("Student not Found")
                
        

    def save_to_file(self):
        data = []
        for student in self.students:
            data.append(student.to_dict())
        with open("students.json", "w") as file:
            json.dump(data,file,indent=4)

        print("Data Saved Successfully")

    def load_from_file(self):
      try:
        with open("students.json","r") as file:
            data = json.load(file)
            self.students = []
            for student_data in data:
                student = Student(
                    student_data["name"],
                    student_data["roll_no"],
                    student_data["age"],
                    student_data["gpa"] 
                    )
                self.students.append(student)
                print("Data Loaded Successfully")
      except (FileNotFoundError, json.JSONDecodeError):
          print("No Saved data found.")


    def run(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Update Student")
            print("4. Search Student")
            print("5. Display All Students")
            print("6. Save Data")
            print("7. Load Data")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.delete_student()

            elif choice == "3":
                self.update_student()

            elif choice == "4":
                self.search_student()

            elif choice == "5":
                self.display_students()

            elif choice == "6":
                self.save_to_file()

            elif choice == "7":
                self.load_from_file()

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()
    