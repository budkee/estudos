"""
    Processamento paralelo sem ligação entre si.
"""

from threading import Thread
import sys

COUNTDOWN = 5

class Th(Thread):

    def __init__ (self, num):
        # Imprimir no console de modo a garantir a ordem do processo
        sys.stdout.write("Making thread number " + str(num) + "\n")
        sys.stdout.flush()
        Thread.__init__(self)
        self.num = num
        self.countdown = COUNTDOWN

    def run(self):

        while (self.countdown):
            sys.stdout.write("Thread " + str(self.num) + " (" + str(self.countdown) + ")\n")
            sys.stdout.flush()
            self.countdown -= 1


for thread_number in range (5):
    thread = Th(thread_number)
    thread.start()



"""
    Referência: https://imasters.com.br/back-end/threads-em-python
"""