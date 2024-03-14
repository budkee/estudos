"""
    Código para realizar o cálculo de 100 elementos de um vetor utilizando 4 threads, dividindo o trabalho em 25 elementos para cada thread. Note que o valor do cálculo sequencial é o mesmo do cálculo em thread.
"""
# Imports
from threading import Thread
import random
import sys

# Configurações do programa
NUM_VALUES = 100
values = []
sequential_total = 0
threaded_total = 0
threads = []
NUM_THREADS = 4

# Construtor de objetos
class Th(Thread):
    
    subtotal = 0

    def __init__ (self, num):

        sys.stdout.write("Making thread number " + str(num) + "\n")
        sys.stdout.flush()

        Thread.__init__(self)
        self.num = num

    def run(self):

        global values
        range_start = int(self.num * NUM_VALUES / NUM_THREADS)
        range_end = int((self.num + 1) * NUM_VALUES / NUM_THREADS)

        for i in range(range_start, range_end):

            self.subtotal += values[i]
            sys.stdout.write(
                "Subtotal for thread " + str(self.num) + 
                ": " + str(self.subtotal) + 
                " (from " + str(range_start) + 
                " to " + str(range_end) + ")\n"
            )
            sys.stdout.flush()

    def get_subtotal(self):
        return self.subtotal

#### O programa comeca aqui #####

#if '__name__'=='__main__':

# Gerando numeros aleatórios
for i in range(NUM_VALUES):
    values.append(random.randint(0,100))

# Calculo sequencial
for i in range(NUM_VALUES):
    sequential_total += values[i]

print("Total em sequência: " + str(sequential_total)) # 1º output

# Iniciando as threads
for thread_number in range(NUM_THREADS):
    threads.insert(thread_number, Th(thread_number))
    threads[thread_number].start()

# Esperando as threads terminarem e somando os subtotais
for thread_number in range(NUM_THREADS):
    threads[thread_number].join()
    threaded_total += threads[thread_number].get_subtotal()

print("Total em thread: " + str(threaded_total)) # Último output


"""
    Referência: https://imasters.com.br/back-end/threads-em-python
"""