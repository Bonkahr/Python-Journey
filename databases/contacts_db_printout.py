import sqlite3

db = sqlite3.connect('contacts.sqlite')

# query a single data from the database
name = input('Enter the name to check data: ')

check_db = "SELECT * FROM contacts WHERE name = ? "

# querying without the case sensitivity
check_db_no_case = "SELECT * FROM contacts WHERE name LIKE ? "

# check.execute(check_db, (name,))


for rows in db.execute(check_db_no_case, (name,)):
    print(rows)

db.close()
