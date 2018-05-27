import threading
import time

#def print_time(name, delay):
def print_time_name(delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
#        print("name: " + name + " " + time.ctime(time.time()))
        print("name: " + threading.current_thread().getName() + " " + time.ctime(time.time()))
#t1 = threading.Thread(target=print_time, args=('watek1', 2))
#t2 = threading.Thread(target=print_time, args=('watek2', 1))
#t3 = threading.Thread(target=print_time, args=('watek3', 4))

t11 = threading.Thread(name='w1', target=print_time_name, args=(2,))
t22 = threading.Thread(name='w2', target=print_time_name, args=(1,))

t11.start()
t22.start()
#t1.start()
#t2.start()
#t3.start()