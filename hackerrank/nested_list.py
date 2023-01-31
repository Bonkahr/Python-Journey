import statistics


def order_students(grades: list):
    ordered_grades = []
    for student in grades:
        ordered_grades.append(student[1])
    ordered_grades = sorted(set(ordered_grades))
    lowest_second_student = []
    for student in grades:
        if student[1] == ordered_grades[1]:
            lowest_second_student.append(student[0])
    return sorted(lowest_second_student)


def average(data: dict, student: str):
    return f'{statistics.mean(data[student]):.2f}'


if __name__ == '__main__':
    student_scores = []
    for _ in range(int(input('Number of students: '))):
        name = input('Enter name: ')
        score = float(input('Enter Grade: '))
        student_scores.append([name, score])

    for x in order_students(student_scores):
        print(x)
