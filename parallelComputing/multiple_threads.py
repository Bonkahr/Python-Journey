import os
import threading


def cpu_waster() -> None:
    """
    Wastes CPU cycles forever
    :return: None
    """
    while True:
        pass


# display info about the process
print('\n Process ID: ', os.getpid())
print('Thread Count: ', threading.active_count())

for thread in threading.enumerate():
    print(thread)

print('\nStarting 8 CPU Wasters....')
for i in range(8):
    threading.Thread(target=cpu_waster).start()

# Display info about the process
print('\nProcess ID/: ', os.getpid())
print('Thread Count: ', threading.active_count())
for thread in threading.enumerate():
    print(thread)
