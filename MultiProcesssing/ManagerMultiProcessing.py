#multiprocessing.Manager: It is used to create a manager that can be shared between processes. 
#It provides a way to share mutable data like lists, dictionaries, and other objects between processes.

import multiprocessing
import time

def worker(shared_list, message):
    time.sleep(1)
    shared_list.append(message)
    print(f"Worker added message: {message}")

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()
        processes = []
        messages = ["Hello from worker 1", "Hello from worker 2", "Hello from worker 3", "Hello from worker 4"]

        for message in messages:
            process = multiprocessing.Process(target=worker, args=(shared_list, message))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        print(f"Final shared list: {list(shared_list)}")