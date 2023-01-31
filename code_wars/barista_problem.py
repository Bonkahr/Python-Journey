def passed(subjects: list) -> str:
    return "Pass" if sum(subjects) / len(subjects) >= 40 \
                     and not [x for x in subjects if x < 33] else "Fail"


def marks():
    subjects = input("Number of subjects examined: ")
    while True:
        try:
            int(subjects)
            break
        except ValueError:
            subjects = input("Number of subjects examined: ")

    subject_marks = []
    for x in range(int(subjects)):
        subject_marks.append(input(f"Enter Marks for subject {x + 1}: "))

    while True:
        try:
            [int(x) for x in subject_marks]
            break
        except ValueError:
            print(f"{subject_marks} <- Check the marks, one or more not "
                  f"an integer.")
            subject_marks = []
            for x in range(int(subjects)):
                subject_marks.append(input(f"Enter Marks for subject"
                                           f" {x + 1}: "))

    return [int(x) for x in subject_marks]


print(passed(marks()))
