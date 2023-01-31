from bmi_calculator import BMI
import sqlite3 as sq


def person():
    def valid_number(i):
        try:
            i = int(i)
            return True
        except ValueError:
            return False

    print("Good choice, please provide the following information ")
    name = input('Please enter your name: ')
    while not name:
        name = input('Please enter a valid name: ')

    age = input('Please enter your age: ')
    while not valid_number(age):
        age = input("Enter a valid age: ")

    weight = input('Please enter your weight in kgs: ')
    while not valid_number(weight):
        weight = input('Please enter a valid weight in kgs: ')

    height = input('Please enter your height in cm: ')
    while not valid_number(height):
        height = input('Please enter a valid height: ')

    return name, age, int(weight), int(height)


choice = input("""Welcome to BMI calculator.
Press Enter to continue:""")

if choice == '':
    n, a, w, h = person()
    p = BMI(n, a, w, h)

    with sq.connect('bmi.db') as connection:
        cursor = connection.cursor()
        query = "SELECT datetime('now', 'localtime');"
        time = cursor.execute(query).fetchone()[0]
        # cursor.execute("CREATE TABLE BMI(Name TEXT, Age TEXT, Weight INT, "
        #                "Height INT, Bmi FLOAT(1), MassIndex TEXT, "
        #                "Registration DATE)")
        data = (n, a, w, h, p.calculate_bmi(), p.bmi_index(), time)

        if p.calculate_bmi() is not None and p.bmi_index() is not None:
            cursor.execute("INSERT INTO BMI VALUES(?,?,?,?,?,?,?)", data)
        else:
            print("Invalid data, please check your Height or Weight")
        cursor.execute("SELECT * FROM BMI")
        for i, person in enumerate(cursor.fetchall()):
            print(f"Number {i}:\n\tName: {person[0]}\n\tAge: {person[1]}\n"
                  f"\tWeight: {person[2]}\n\tHeight: {person[3]} "
                  f"\n\tBMI: {person[4]}\n\tStatus: {person[5]}\n\tDate "
                  f"Entered: {person[6]}")

        # print(f"Hello {n}, you are {p.bmi_index()} with BMI of {
        # p.calculate_bmi()}")
