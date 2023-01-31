import sqlite3

# connection to database and creating a database
db = sqlite3.connect('contacts.sqlite')

# creating a table if doesn't exist
db.execute('CREATE TABLE IF NOT EXISTS contacts(name Text, '
           'phone INTEGER, email TEXT)')

# inserting a record or row
db.execute(
    "INSERT INTO contacts(name, phone, email)VALUES('JAMES', 123, "
    "'james@gmail.com')")

# inserting data without indicating the table heads
db.execute(
    "INSERT INTO contacts VALUES('Daniel', 09876543, 'daniel@gmail.com')")

# querying data from the database
cursor = db.cursor()    # cursor() is a generator

cursor.execute("SELECT * FROM contacts")

# # the cursor outputs a tuple of the row which is iterable
# for row in cursor:
#     print(row)

# fetch all data from the database, returns a list of tuples
print(cursor.fetchall())

# fetch one returns tuple per row
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())


# after reading data from a database the data can't be read again in cursor'
# unpacking the tuple above
for name, phone, email in cursor:
    print(f'Name: {name}, Phone: {phone} Email: {email}')
    print('*' * 80)

# closing the cursor
cursor.close()
# data_base.commit()

# committing the data to be saved, the program is run again and again the
# data is stored duplicating the record
db.commit()
db.close()
