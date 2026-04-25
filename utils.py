def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "c"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_percentage(marks_obtained, max_marks):
    return round((marks_obtained / max_marks) * 100, 2)


# if __name__ == "__main__":
#     percentage = calculate_percentage(95, 100)
#     grade = calculate_grade(percentage)
#     print(f"Percentage: {percentage}%")
#     print(f"Grade: {grade}")
