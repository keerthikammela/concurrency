#Handling synchronization in the program execution while using multithreading

import threading
import time

lock = threading.Lock()

data = None

def fetch_data():
    global data
    with lock:  
        print("Thread 1: Fetching data from file...")
        time.sleep(3)
        data = "File content: Hello, this is the data from the file."
        print("Thread 1: Data fetched!")

def process_data():
    with lock:
        while data is None:
            print("Thread 2: Waiting for data to be fetched...")
            time.sleep(1)
        print(f"Thread 2: Processing data: {data}")
        time.sleep(2)
        print("Thread 2: Data processed!")

fetch_data()
process_data()

fetch_thread = threading.Thread(target=fetch_data)
process_thread = threading.Thread(target=process_data)

fetch_thread.start()
process_thread.start()

fetch_thread.join()
process_thread.join()

print("Both threads have completed their tasks.")
