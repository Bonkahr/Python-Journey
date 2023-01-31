import math


def add_time(time: str, duration: str, day='') -> str:
    t = time.split(' ')
    hours = int(t[0].split(':')[0])
    minutes = int(t[0].split(':')[1])
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    time_minutes = minutes + duration_minutes
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday']
    if time_minutes > 60:
        time_minutes -= 60
        hours += 1
    time_hours = hours + duration_hours
    count = 0
    am_pm = t[1]
    while time_hours > 12:
        time_hours -= 12
        count += 1
        if am_pm == 'AM':
            am_pm = 'PM'
        else:
            am_pm = 'AM'
    day_count = count // 2
    to_return = f"{str(time_hours).zfill(2)}:{str(time_minutes).zfill(2)}" \
                f" {am_pm}"
    if day_count == 0 and day:
        to_return += f' ({day})'
    elif day_count == 1:
        if day != '':
            d = days.index(day.lower())
            if d == 6:
                to_return += f' {days[0].title()} (Next day)'
            else:
                to_return += f' {days[d + 1].title()} (Next day)'
        else:
            to_return += f' (Next day)'

    elif day_count > 2:
        if day:
            to_return += f' ({day_count}s later)'
        to_return += f' ({day_count} days later)'
    return to_return


print(add_time("11:30 AM", "13:32", "thUrsDay"))
print(add_time("11:43 AM", "00:20"))
print(add_time("6:30 PM", "205:12"))
print(add_time("11:43 PM", "24:20", "tueSday"))

