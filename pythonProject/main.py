from math import e

name = "James"
age = 21
origin = "Kenya"
nationality = "Kenyan"
name_error = "we have no idea who the fuck you are"

verify_name = input("what,s your name? ")
verify_age = input("whats is yor age? ")
try:
    verify_age = int(verify_age)
except e:
    print("We can only accept numbers on that")
    verify_age = 0

verify_country = input("where are you from? ")

verify_name = verify_name.capitalize()
verify_country = verify_country.capitalize()

if name != verify_name:
    print("Your name isn't correct")

elif verify_age != age:
    if verify_age < age:
        print("I know you are older than that")
    else:
        print("You are too young for that age")

elif origin != verify_country:
    print("That's not your country")

else:
    print("His name is", name, "aged", age, 'a',
          nationality, "from", origin)

if name != verify_name:
    print("That name isn't correct")
    if age != verify_age:
        print("That age isn't correct")
        if origin != verify_country:
            print("That's not your country so ....")
            print("You are not one of us")
            print(name_error)
