from db import get_connection
from student import view_all_students
from subject import view_all_subjects
from utils import calculate_grade, calculate_percentage


def enter_marks():
    view_all_students()
    std_id = int(input("Enter student ID: "))

    view_all_subjects()
    sub_id = int(input("\nEnter subject ID: "))

    marks_obtained = int(input("\nEnter marks obtained: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO grades (std_id, sub_id, marks_obtained) VALUES (%s, %s, %s)"
    cursor.execute(query, (std_id, sub_id, marks_obtained))
    connection.commit()

    print("Marks entered successfully!")
    cursor.close()
    connection.close()


# if __name__ == "__main__":
#     enter_marks()


def view_report_card():
    view_all_students()
    std_id = int(input("\nEnter Student ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT subjects.sub_name, grades.marks_obtained, subjects.max_marks
        FROM grades
        JOIN subjects
        On grades.sub_id = subjects.sub_id
        WHERE grades.std_id = %s
    """
    cursor.execute(query, (std_id,))
    result = cursor.fetchall()

    if len(result) == 0:
        print("No marks found for this student!")
    else:
        print("\n--- Report Card ---")
        total_marks = 0
        total_max = 0
        for row in result:
            percentage = calculate_percentage(row[1], row[2]) # type: ignore
            grade = calculate_grade(percentage)
            print(
                f"Subject: {row[0]} | Marks: {row[1]} | Percentage: {percentage}% | Grade: {grade}") # type: ignore
            total_marks += row[1] # type: ignore
            total_max += row[2] # type: ignore

        total_percentage = calculate_percentage(total_marks, total_max)
        total_grade = calculate_grade(total_percentage)
        print(
            f"\nTotal: {total_marks}/{total_max} | Percentage: {total_percentage}% | Grade: {total_grade}")

    cursor.close()
    connection.close()


# if __name__ == "__main__":
#     view_report_card()


def leaderboard():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT students.std_name, SUM(grades.marks_obtained) as total_marks, SUM(subjects.max_marks) as total_max
        FROM grades
        JOIN students ON grades.std_id = students.std_id
        JOIN subjects ON grades.sub_id = subjects.sub_id
        GROUP BY students.std_id, students.std_name
        ORDER BY total_marks DESC
    """
    cursor.execute(query)
    result = cursor.fetchall()

    print("\n--- Leaderboard ---")
    rank = 1
    for row in result:
        percentage = calculate_percentage(row[1], row[2]) # type: ignore
        grade = calculate_grade(percentage)
        print(
            f"Rank: {rank} | Name: {row[0]} | Total: {row[1]}/{row[2]} | Percentage: {percentage}% | Grade: {grade}") # type: ignore
        rank += 1

    cursor.close()
    connection.close()


# if __name__ == "__main__":
#     leaderboard()
