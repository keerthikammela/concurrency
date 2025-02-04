# For tasks that are more data-parallel, you can use multiprocessing.Pool.
# This is a more efficient way to manage multiple processes when you have a large number of tasks to execute.

# Each process has its own memory space, which means no shared memory access. 
# This avoids issues like race conditions that are common in multithreading.

# Instead of manually managing each process, we can use a pool of worker processes to handle the computation.

import multiprocessing

def square(number):
    return number ** 2

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    
    print(f"Squares: {results}")
