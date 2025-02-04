# multiprocessing creates separate processes that each have their own memory space,
#  making it more suitable for CPU-bound operations.

# Multiprocessing is best suited for CPU-intensive tasks, like heavy calculations,
# where you need to take advantage of multiple CPU cores. Python’s Global Interpreter Lock (GIL) 
# prevents multiple threads from executing Python bytecodes in parallel, but with multiprocessing,
# each process runs in its own Python interpreter and has its own GIL. 

# Since each process runs independently, you can utilize multiple CPU cores effectively, 
# which can speed up the execution time for certain tasks.

import multiprocessing
import time

def square(number):
    print(f"Calculating square of {number}")
    time.sleep(1)
    result = number ** 2
    print(f"Square of {number} is {result}")

if __name__ == "__main__":

    process1 = multiprocessing.Process(target=square, args=(2,))
    process2 = multiprocessing.Process(target=square, args=(3,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes finished.")
