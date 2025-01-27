def get_student_details():
    students = []
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        student = {
            'name': name,
            'age': age,
            'grade': grade
        }
        students.append(student)
    return students

def main():
    student_list = get_student_details()
    print("Student Details:")
    for student in student_list:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

if __name__ == "__main__":
    main()