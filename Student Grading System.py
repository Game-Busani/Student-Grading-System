
# Initialize an empty dictionary to store student data
students = {}

# ask the user to enter the number of students in the class
num_students = int(input("Enter the number of students: "))

#establish a a list of subjects
subjects = ['Math', 'English', 'Science', 'Setswana', 'Economics']

#Loop through the range of students to get their names and grades
for i in range(num_students):
    #prompt user to enter the student' name
    name = input(f"Enter the name of student {i + 1}: ")

    #create a dictionary to store grades for each subject
    grades = {}

    #loop to insert grades for each subject
    for subject in subjects:
        while True:
            try:
                #ask user to enter the student's grade for specific subject
                grade = float(input(f"Enter the grade for {name} in {subject}: "))
                #ensure that the grade entered is within the 0-100 range
                if 0 <= grade <= 100:
                    grades[subject] = grade  # Add the grade to the dictionary
                    break
                else:
                    print("Grade must be between 0 and 100. Enter grade again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    #merge the student's grades dictionary w the students dictionary
    students[name] = grades

#functionality to add a new student
def add_student():
    name = input("Enter the name of the new student: ")
    grades = {}
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter the grade for {name} in {subject}: "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                else:
                    print("Grade must be between 0 and 100. Enter grade again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    students[name] = grades
    print(f"{name} has been added to the system.")

#Functionalit to update a student'sgrade
def update_grade():
    name = input("Enter the name of the student to update: ")
    if name in students:
        subject = input("Enter the subject to update: ")
        if subject in subjects:
            while True:
                try:
                    grade = float(input(f"Enter the new grade for {name} in {subject}: "))
                    if 0 <= grade <= 100:
                        students[name][subject] = grade
                        print(f"Updated {name}'s grade in {subject} to {grade}.")
                        break
                    else:
                        print("Grade must be between 0 and 100. Enter grade again.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid subject.")
    else:
        print(f"{name} not found.")

#Functionality to remove a student
def remove_student():
    name = input("Enter the name of the student to remove: ")
    if name in students:
        del students[name]
        print(f"{name} has been removed from the system.")
    else:
        print(f"{name} not found.")

# Functionality to view all student grades for aspecific subject and the subject average
def view_subject_grades():
    subject = input("Enter the subject to view grades for: ")
    if subject in subjects:
        print(f"\nGrades for {subject}:")
        total = 0
        count = 0
        for name, grades in students.items():
            grade = grades.get(subject, 'N/A')
            if grade != 'N/A':
                total += grade
                count += 1
            print(f"{name}: {grade}")
        if count > 0:
            subject_average = total / count
            print(f"\nAverage Grade for {subject} is {subject_average:.2f}")
        else:
            print(f"No grades recorded for {subject}.")
    else:
        print("Invalid subject.")

#Functionality to search for a student and retrieve their grades and totaaverage
def search_student():
    name = input("Enter the name of the student to search for: ")
    if name in students:
        grades = students[name]
        print(f"\n{name}'s Grades:")
        for subject, grade in grades.items():
            print (f"{subject}: {grade}")
        average = sum(grades.values()) / len(grades)
        print(f"Average Grade: {average:.2f}")
    else:
        print(f"{name} not found.")

#Functionality to sort students by name or thei averages
def sort_students():
    criteria = input("Sort students by their 'Name' or 'Average': ").strip().lower()

    if criteria not in ['name', 'average']:
        print("Invalid sorting criteria. Pick 'Name' or 'Average'.")
        return

    #ask the user to select order for sorting
    print("Choose sorting order:")
    print("1. Ascending Order")
    print("2. Descending")
    order_choice = input("Enter choice (1 or 2): ").strip()

    # Determine sorting order based on user choice
     #Ascending
    if order_choice == '1':
        reverse = False
        #descending
    elif order_choice == '2':
        reverse = True   
    else:
        print("Invalid choice. Please pick '1' for Ascending or '2' for Descending.")
        return

    #sorting based on the selected order
    if criteria == 'name':
        sorted_students = sorted(students.items(), key=lambda x: x[0].lower(), reverse=reverse)
    elif criteria == 'average':
        sorted_students = sorted(students.items(), key=lambda x: sum(x[1].values()) / len(x[1]), reverse=reverse)

    #displaying sorted students with their averages
    print("\nSorted Students:")
    for name, grades in sorted_students:
        average = sum(grades.values()) / len(grades)
        print(f"{name}: Average Grade = {average:.2f}")


#print the menu for users
def menu():
    while True:
        print("\n1. Add A Student")
        print("2. Update A Grade")
        print("3. Remove A Student")
        print("4. View Grades for A Subject")
        print("5. Search For Student")
        print("6. Sort Students")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            update_grade()
        elif choice == '3':
            remove_student()
        elif choice == '4':
            view_subject_grades()
        elif choice == '5':
            search_student()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

#run program
menu()



