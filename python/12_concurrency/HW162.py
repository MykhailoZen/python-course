import concurrent.futures
import asyncio
import random
import time
import threading

# Function for sleeping for a random amount of time
def sleep_random():
    duration = random.uniform(0, 10)
    time.sleep(duration)
    # Print the sleep duration and thread ID
    print(f"Thread {threading.get_ident()} slept for {duration:.2f} seconds")
    return duration

# Function for executing the multithreading task
def multithreading_task(num_threads):
    # Use ThreadPoolExecutor to execute tasks in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Submit tasks to the executor and get their futures
        futures = [executor.submit(sleep_random) for _ in range(20)]
        # Wait for all tasks to complete and collect their results
        total_workload = sum(future.result() for future in concurrent.futures.as_completed(futures))
        max_workload = max(future.result() for future in concurrent.futures.as_completed(futures))
    # Print total and max workload times
    print(f"Total workload time: {total_workload:.2f} seconds")
    print(f"Max workload time: {max_workload:.2f} seconds")

# Function for asynchronous sleeping
async def async_sleep_random():
    duration = random.uniform(0, 10)
    # Asynchronously sleep for a random duration
    await asyncio.sleep(duration)
    # Print the sleep duration and task ID
    print(f"Task {id(asyncio.current_task())} slept for {duration:.2f} seconds")
    return duration

# Function for executing the asyncio task
async def asyncio_task(num_tasks):
    # Create tasks for asynchronous sleeping
    tasks = [asyncio.create_task(async_sleep_random()) for _ in range(num_tasks)]
    # Wait for all tasks to complete and collect their results
    results = await asyncio.gather(*tasks)
    total_workload = sum(results)
    max_workload = max(results)
    # Print total and max workload times
    print(f"Total workload time: {total_workload:.2f} seconds")
    print(f"Max workload time: {max_workload:.2f} seconds")

if __name__ == "__main__":
    start = time.time()

    # Execute the multithreading task with 5 threads
    multithreading_task(5)

    # Print the elapsed time for multithreading
    print(f"Elapsed time for multithreading: {time.time() - start:.2f} seconds")

    start = time.time()

    # Execute the asyncio task with 20 tasks
    asyncio.run(asyncio_task(20))

    # Print the elapsed time for asyncio
    print(f"Elapsed time for asyncio: {time.time() - start:.2f} seconds")
