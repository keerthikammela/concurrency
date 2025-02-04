# Asynchronous programming is a concurrency technique that allows tasks to run concurrently
# without being blocked by others.

# The mechanism that schedules and manages asynchronous tasks.
# It ensures that coroutines run when they are ready (i.e., once the awaited task is completed).

import asyncio

async def fetch_data_from_server(server_id):
    print(f"Fetching data from server {server_id}...")
    await asyncio.sleep(3)
    return f"Data from server {server_id}"

async def main():
    tasks = [fetch_data_from_server(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    
    for result in results:
        print(f"Processed: {result}")

asyncio.run(main())
