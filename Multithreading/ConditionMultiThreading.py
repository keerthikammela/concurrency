# The threading.Condition() is a synchronization primitive that allows one thread to signal other threads 
# about a condition (like when a shared resource has been updated or is ready for use).

import threading
import time

condition = threading.Condition()
data = None

def fetch_data():
    global data
    with condition:
        print("Fetching data...")
        time.sleep(2)
        data = "Data fetched"
        print("Data fetched!")
        condition.notify()

def process_data():
    with condition:
        while data is None:
            print("Waiting for data...")
            condition.wait()
        print(f"Processing: {data}")

thread1 = threading.Thread(target=fetch_data)
thread2 = threading.Thread(target=process_data)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished execution.")