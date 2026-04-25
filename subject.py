from db import get_connection

def add_subject():
    subject_name = input("Enter subject name: ")
    max_marks = input("Enter max marks: ")
    
    connection = get_connection()
    cursor = connection.cursor()
    
    query = "INSERT INTO subjects(sub_name, max_marks) VALUES (%s, %s)"
    cursor.execute(query, (subject_name, max_marks))
    connection.commit()
    
    print("Subject added successfully!")
    cursor.close()
    connection.close()
    
# if __name__ == "__main__":
#     add_subject()
    
def view_all_subjects():
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    
    if len(subjects) == 0:
        print("No subjects found!")
    else:
        print("|n--- All Subjects ---")
        for subject in subjects:
            print(f"ID: {subject[0]} | Subject: {subject[1]} | Max Marks: {subject[2]}")
    cursor.close()
    connection.close()
    
# if __name__ == "__main__":
#     view_all_subjects()
    
def delete_subjects():
    view_all_subjects()
    subject_id = int(input("\nEnter subject ID to delete: "))
    
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM subjects WHERE sub_id = %s", (subject_id,))
    connection.commit()
    
    print("Subject deleted seccessfully!")
    cursor.close()
    connection.close()
    
# if __name__ == "__main__":
#     delete_subjects()
    