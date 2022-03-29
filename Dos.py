import threading
import keyboard
import os
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
rangeOf = 16
threads = []
Target = '192.1.0.0'
def do_requests():
    while True:
        if keyboard.is_pressed('X'):
            print('| ',current_time, " | Q U I T ")
            break
        print('| ',current_time)
        os.system('ping '+ Target)
for i in range(rangeOf):
    t = threading.Thread(target=do_requests)
    t.daemon = True
    threads.append(t)
for i in range(rangeOf):
    threads[i].start()
for i in range(rangeOf):
    threads[i].join()