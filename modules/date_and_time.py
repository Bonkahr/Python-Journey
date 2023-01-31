import time
print(time.gmtime(0))
print(time.localtime())
print(time.time())

time_now = time.localtime()
print("Year:", time_now.tm_year)
print("Month:", time_now.tm_mon)
print("Day: ", time_now.tm_mday)

