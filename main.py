from student import add_student, view_all_students, delete_student
from subject import add_subject, view_all_subjects, delete_subjects
from grades import enter_marks, view_report_card, leaderboard


def main():
    while True:
        print("\n==== Student Grade Tracker ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Students")
        print("4. Add Subjects")
        print("5. View all subjects")
        print("6. Delete Subjects")
        print("7. Enter Marks")
        print("8. View Report Card")
        print("9. View Leaderboard")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            add_subject()
        elif choice == "5":
            view_all_subjects()
        elif choice == "6":
            delete_subjects()
        elif choice == "7":
            enter_marks()
        elif choice == "8":
            view_report_card()
        elif choice == "9":
            leaderboard()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
