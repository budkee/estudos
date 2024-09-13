from multiprocessing import Process
from threading import Thread
from time import sleep
import random

shared_x = random.randint(10,99)

# Processo 1
def sleeping(name):
    global shared_x
    s = random.randint(1,20)
    sleep(s)
    shared_x = shared_x + 1

# Processo 2
def sleeper(name):
    
    sleeplist = list()

    for i in range(3):
        subsleeper = Thread(target=sleeping, args=(name+" "+str(i),))
        sleeplist.append(subsleeper)
    
    for s in sleeplist: s.start()
    for s in sleeplist: s.join()


if __name__ == "__main__":
    
    p = Process(target=sleeper, args=("eve",))
    q = Process(target=sleeper, args=("bob",))
    p.start(); q.start()
    p.join(); q.join()  