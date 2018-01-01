"""
Name:
TRACE folder:
Date:
Lab on class variables, pickling and exceptions
"""
from student import Student
import pickle

def addStudentsToFile(students):
    """writes all Student objects in the list parameter to the file students.dat"""
    f=open('students.dat','wb')
    for student in students:
        pickle.dump(student,f)
    f.close()

def displayFromFile():
    """reads objects from the file students.dat and prints them to the screen"""
    f=open('students.dat','rb')
    while True:
        try:
            student=pickle.load(f)
            print(student)
        except EOFError:
            f.close()
            break

def main():
    
    #Create a list with 5 students
    students = []
    for i in range(1,6):
        students.append(Student("Name" + str(i), 3))

    print("Number of student objects created is", Student.COUNT)

    addStudentsToFile(students)
    displayFromFile()

main()
