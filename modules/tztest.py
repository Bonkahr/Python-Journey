import pytz
import datetime

country = 'Africa/Nairobi'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print(("UTC is {}".format(datetime.datetime.utcnow())))

# listing all valid country strings
# for countries in pytz.all_timezones:
#     print(countries)

# for country in sorted(pytz.country_names):
#     print(country + ": " + pytz.country_names[country])

# listing country time zones

# for country in sorted(pytz.country_names):
#     print("{}: {}: {}".format(country, pytz.country_names[country],
#                               pytz.country_timezones.get(country)))

for country in sorted(pytz.country_names):
    print("{}: {}".format(country, pytz.country_names[country]), end=": ")
    if country in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[country]):
            tz_displays = pytz.timezone(zone)
            time_local = datetime.datetime.now(tz=tz_displays)
            print("\t\t{}: {}".format(zone, time_local))
    else:
        print("\t\tNo time zone to show")
