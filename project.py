
class StudentList:
    def __init__(self):
        self.students = []
        self.stdCount = 0
    def addStudent(self):
            studentName = input("Enter the student's name: ")
            if(self.stdCount < 100):
                self.students.append(studentName)
                print("Student record added successfully.")
                self.stdCount += 1
            else:
                print("Error: Maximum number of students reached.")
    def findStudent(self):
        studentName = input("Enter the student's name: ")

        for i in range(self.stdCount):
            if self.students[i] == studentName:
                return i
        print("Error: Student record not found.")
        return -1
    def deleteStudent(self):
        index = self.findStudent()
        if index != -1:
            self.students.pop(index)
            self.stdCount -= 1
            print("Student record deleted successfully.")
    def searchStudent(self):
        index = self.findStudent()
        if index != -1:
            print("Student record found.")
    def displayAllStudents(self):
        if(self.stdCount > 0):
            print("Student Records:\n"+
                    "----------------")
            for student in self.students:
                print(student)
        else:
            print("No student records found.")
running = True
studentList = StudentList()
while running:
    print("---------------------------------\n"
            +"Student Record Management System\n"
            +"---------------------------------\n"
            +"1. Add a new student record\n"
            +"2. Delete student record\n"
            +"3. Search for a student record\n"
            +"4. Display all student records\n"
            +"5. Exit")
    userIn = input("Enter your choice(1-5): ")
    print()
    if(userIn == "1"):
        studentList.addStudent()
    elif(userIn == "2"):
        studentList.deleteStudent()
    elif(userIn == "3"):
        studentList.searchStudent()
    elif(userIn == "4"):
        studentList.displayAllStudents()
    elif(userIn == "5"):
        running = False
        print("Thank you for using the Student Record Management System!")
    else:
        print("Invalid Choice. Please try again.")
    print()