import time
import threading

semaphore =  threading.Semaphore(5)

def waiting_space(person):
    print(f'{person} is trying to enter session.')
    semaphore.acquire()
    print(f'{person} entered in session.')
    time.sleep(5)
    print(f'{person} bought the ticket')
    semaphore.release()

persons = ['Akaki', 'Nino', 'Gela', 'Naniko', 'Giorgi', 'Magda', 'Soso', 'Irakli', 'Marika', 'Luka', 'Eto', 'Irakli', 'Kakha', 'Lena', 'Bakuri']

start = time.perf_counter()

threads = [threading.Thread(target=waiting_space, args=(person,)) for person in persons]

for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

end = time.perf_counter()
delta = end - start
print(f"It's needed {delta:.2f} seconds for sell 15 tickets.")
