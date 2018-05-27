import threading
import time

def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("name: " + name + " " + time.ctime(time.time()))

t1 = threading.Thread(target=print_time, args=('watek1', 2))
t2 = threading.Thread(target=print_time, args=('watek2', 1))
t3 = threading.Thread(target=print_time, args=('watek3', 4))

t1.start()
t2.start()
t3.start()