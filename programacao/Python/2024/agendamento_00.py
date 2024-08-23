import schedule
import time

def job():
    print("Esse é o resultado do meu trabalho.")


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(4)