import time
print("time():\t\t", time.get_clock_info("time"))
print("monotonic():", time.get_clock_info("monotonic"))
print("perf_counter():\t", time.get_clock_info("perf_counter"))
print("process_counter():\t", time.get_clock_info("process_time"))
