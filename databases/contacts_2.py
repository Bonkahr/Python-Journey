import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = "anotherupdates@email.com"
phone = input('please enter the phone number: ')

# updating contacts with the phone number given
# update_sql = "UPDATE contacts SET email='{}' WHERE phone={}".format(
#     new_email, phone)

# using place holders (?) to prevents sql injection
update_sql = "UPDATE contacts SET email= ? WHERE phone= ?"

# using cursor to connect to connection and to update the record
update_cursor = db.cursor()

# executing the update
# update_cursor.execute(update_sql)

# updating the database using the placeholders variables inert a tuple of
# variables
update_cursor.execute(update_sql, (new_email, phone))


# printing the number of rows the cursor updated
print(f'{update_cursor.rowcount} rows updated')

# committing the changes to the contacts database, recommended to use cursor
# instead of the connection
update_cursor.connection.commit()

# closing the cursor update
# update_cursor.connection is same(==) as db.
update_cursor.close()

# iterating through the database without using a cursor
# without committing the data in contacts.py the contacts are not not written to
# the database hence the following code results to no output if commit
# statement not included
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(f'Name: {name}, Phone: {phone}, Email: {email}')

# always commit your changes when you are happy with the changes, always
# recommended to use the cursor commit method instead of the connection
# db.commit()
db.close()
