#   multithreading 
#   -------------- 
#   multiple threads are created within a single process to perform concurrent tasks.
#   These threads share the same memory space and resources.

import threading
import time

def print_numbers(thread_name, count):
    for i in range(count):
        time.sleep(3)  # Simulate some delay (e.g., I/O wait)
        print(f"{thread_name} - Number: {i}")

# Create two threads to run the print_numbers function concurrently
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 5))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish before continuing
thread1.join()
thread2.join()

print("Both threads have finished execution.")

