import threading
import time

def daemonThread():
    print('Starting')
    time.sleep(5)
    print('Exiting')

def nonDaemonThread():
    print('Starting')
    time.sleep(2)
    print('Exiting')

#logging.basicConfig(level=logging.DEBUG, format='(%(threadName)=10s)%(message)s',)

d = threading.Thread(name='daemonThread', target=daemonThread, daemon=True)
t = threading.Thread(name='nonDaemonThread', target=nonDaemonThread, daemon=True)

print(threading.enumerate())

d.start()
t.start()
d.join()
#main_thread = threading.main_thread()

print(threading.enumerate())

d.start()
print(threading.enumerate())
'''for th in threading.enumerate():
    if th is main_thread:
        continue
    print('join ' + x.getName())
    th.join()'''