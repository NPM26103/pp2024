#Uncomment the following block to input students info...
'''def students_info():
    s_num = int(input("Enter the number of students in the class: "))
    students = []
    for i in range(s_num):
        s_id = input(f"Enter student {i + 1} ID: ")
        s_name = input(f"Enter student {i + 1} name: ")
        DOB = input(f"Enter student {i + 1} date of birth: ")
        s_info = {'id': s_id, 'name': s_name, 'DOB': DOB, 'marks': {}}
        students.append(s_info)
    return students'''

#Uncomment the following block to input courses info...
'''def courses_info():
    c_num = int(input("Enter the number of courses: "))
    courses = []
    for i in range(c_num):
        c_id = input(f"Enter course {i + 1} ID: ")
        c_name = input(f"Enter course {i + 1} name: ")
        c_info = {'id': c_id, 'name': c_name}
        courses.append(c_info)
    return courses'''

def marks(students, courses):
    course_id = input("Enter the course ID to input marks: ")
    for c in courses:
        if c['id'] == course_id:
            for s in students:
                mark = float(input(f"Enter marks for {s['name']} in {c['name']}: "))
                s['marks'][c['id']] = mark
            return
    print("Course not found!")

def display(students, courses):
    print("\nList of courses:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}\n")

    print("List of students:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DOB: {s['DOB']}\n")

def show_marks(students, courses):
    student_id = input("Enter student ID to show marks: ")
    for s in students:
        if s['id'] == student_id:
            print(f"\nMarks for {s['name']}:")
            for c in courses:
                mark = s['marks'].get(c['id'], "N/A")
                print(f"{c['name']}: {mark}")
            return
    print("Student not found!")

def main():

    #Students data
    try:
        students = students_info()
    except:
        students = [{'id': "1", 'name': "NPM", 'DOB': "1/1/1", 'marks': {}},
                    {'id': "2", 'name': "NPM_nhung_la_id_2", 'DOB': "2/2/2", 'marks': {}},
                    {'id': "3", 'name': "van_la_NPM_nhung_id_3", 'DOB': "3/3/3", 'marks': {}}]

    #Courses data
    try:
        courses = courses_info()
    except:
        courses = [ {'id': "1", 'name': "Python"},
                    {'id': "2", 'name': "OOP"},
                    {'id': "3", 'name': "Prob"}]

    display(students, courses)
    while True:
        print("\nMenu:")
        print("1. Input marks")
        print("2. Show student marks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            marks(students, courses)
        elif choice == '2':
            show_marks(students, courses)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3!")

if __name__ == "__main__":
    main()


