cities = ['Nairobi', 'Thika', 'Mombasa', 'Kisumu']

with open("cities.txt", 'w') as cities_file:
    for city in cities:
        print(city, file=cities_file)

with open("cities.txt", 'r') as city_file:
    for line in city_file:
        print(line, end="")
