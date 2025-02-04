#If you need to share data between processes, you can use multiprocessing.Queue, 
# multiprocessing.Pipe, or multiprocessing.Manager.

import multiprocessing

def worker(queue, message):
    queue.put(message)

if __name__ == "__main__":

    queue = multiprocessing.Queue()
    processes = []
    messages = ["Hello from worker 1", "Hello from worker 2", "Hello from worker 3", "Hello from worker 4"]
    
    for i, message in enumerate(messages):
        process = multiprocessing.Process(target=worker, args=(queue, message))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    while not queue.empty():
        print(f"Message from worker: {queue.get()}")

