
# Sequential Dependency (One Thread Waits for Another to Finish): In some cases, one thread must wait 
# for another thread to complete its task before proceeding. You can use synchronization mechanisms 
# such as Locks.

# A lock ensures that only one thread can execute the critical section of code at a time

import threading
import time

lock = threading.Lock()
data = []

def fetch_data_from_file(file_name):
    with lock:
        print(f"Fetching data from {file_name}...")
        time.sleep(1)
        data.append(f"Content from {file_name}")
        print(f"Data fetched from {file_name}")

def process_data():
    with lock:
        while len(data) == 0:
            print("Waiting for data to be fetched...")
            time.sleep(1)
        print("Processing data...")
        time.sleep(2)
        print(f"Processed data: {data}")

files_to_fetch = ['file1.txt', 'file2.txt', 'file3.txt']
threads = []

for file in files_to_fetch:
    thread = threading.Thread(target=fetch_data_from_file, args=(file,))
    threads.append(thread)
    thread.start()

process_thread = threading.Thread(target=process_data)
process_thread.start()

for thread in threads:
    thread.join()

process_thread.join()

print("All tasks are complete.")
