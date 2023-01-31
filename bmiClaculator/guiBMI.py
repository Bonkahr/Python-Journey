from bmi_calculator import BMI
import sqlite3 as sq
import easygui as gui


def person():
    def valid_number(i):
        try:
            i = int(i)
            return True
        except ValueError:
            return False

    accepted = gui.msgbox(msg="Good choice, please provide the following "
                              "information",
                          ok_button='Ok',
                          title='Do you wish to continue?'
                          )
    if accepted is None:
        exit()

    name = gui.enterbox(msg='Please enter your name..', title='Name')
    while not name:
        name = gui.enterbox(msg='Please enter a valid name.', title='Name')
    if name is None:
        exit()

    age = gui.enterbox(msg='Please enter your age...', title='Enter your Age')
    while age is None or not valid_number(age):
        age = gui.enterbox(
            msg='Please enter your age...',
            title='Enter valid Age',
        )

    weight = gui.enterbox(
        'Please enter your weight in kgs: ',
        title='Enter your Weight'
    )
    while weight is None or not valid_number(weight):
        weight = gui.enterbox(
            'Please enter a valid weight in kgs: ',
            title='Enter your Weight'
        )

    height = gui.enterbox(
        'Please enter your height in cm: ',
        title='Enter your height'
    )
    while height is None or not valid_number(height):
        height = gui.enterbox(
            'Please enter your height in cm: ',
            title='Enter your height'
        )

    return name, age, int(weight), int(height)


choice = gui.msgbox('Welcome to BMI calculator.', ok_button='Continue')

if choice == 'Continue':
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
        # cursor.execute("SELECT * FROM BMI")
        # print(cursor.fetchall())
