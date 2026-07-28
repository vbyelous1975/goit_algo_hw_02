from queue import Queue
import random


q = Queue()

def generate_request():
    request = random.randint(1,1000)
    q.put(request)
    return request
def process_request():
    if q.empty() == False:
        print(f"Заявка за номером:{q.get()} успішно оброблена")
    else:
        print("Черга пуста")


print(f"Ваша заявка за номером {generate_request()} додана до черги")
print(f"Ваша заявка за номером {generate_request()} додана до черги")
print(f"Ваша заявка за номером {generate_request()} додана до черги")

process_request()
process_request()
process_request()
process_request()