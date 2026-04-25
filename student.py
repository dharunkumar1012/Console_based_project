from db import get_connection


def add_student():
    name = input("Enter your name:")
    email = input("Enter your email:")
    ph_no = input("Enter your number:")
    cls = input("Enter your class:")

    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO students (std_name, std_email, ph_no, class) VALUES (%s, %s,%s,%s)"
    cursor.execute(query, (name, email, ph_no, cls))
    connection.commit()

    print("Student added successfully!")
    cursor.close()
    connection.close()


# if __name__ == "__main__":
#     add_student()


def view_all_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found!")
    else:
        print("\n--- All Students ---")
        for student in students:
            print(
                f"ID: {student[0]} | Name: {student[1]} | Email: {student[2]} | Phone: {student[3]} | Class: {student[4]}")
    cursor.close()
    connection.close()


# if __name__ == "__main__":
#     view_all_students()


def delete_student():
    view_all_students()
    student_id = int(input("\nEnter student ID to delete:"))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE std_id = %s", (student_id,))
    connection.commit()

    print("Student deleted successfully")
    cursor.close()
    connection.close()


# if __name__ == "__main__":
#     delete_student()

