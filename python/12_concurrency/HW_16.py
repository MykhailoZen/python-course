#Multiprocessing, CPU-bound work (30 points):
import multiprocessing
import time
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))
def calculate_sum_parallel(start: int, end: int, chunk_size: int = 1000000) -> int:
    total_sum = 0
    num_chunks = (end - start + 1) // chunk_size + ((end - start + 1) % chunk_size > 0)
    multiprocessing.set_start_method('fork')
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.starmap(calculate_sum, [(start + i * chunk_size,
                                                min(start + (i + 1) * chunk_size - 1, end))
                                               for i in range(num_chunks)])
        total_sum = sum(results)

    end_time = time.time()
    print(f"Duration of parallel approach: {end_time - start_time} sec")

    return total_sum

start = 1
end = 2**30

start_time2 = time.time()
result_sequential = calculate_sum(start, end)
end_time2 = time.time()
print(f"Duration of sequential approach: {end_time2 - start_time2} sec")
print(f"Sum of numbers in the given range from {start} to {end} using sequential approach: {result_sequential}")

result_parallel = calculate_sum_parallel(start, end)
print(f"Sum of numbers in the given range from {start} to {end} using parallel approach: {result_parallel}")

#Multithreading, IO-bound work (30 points):
import random
from concurrent.futures import ThreadPoolExecutor

def sleeping():
    sleep_duration = random.randint(1, 5)
    time.sleep(sleep_duration)
    print(f"Sleeping {sleep_duration} seconds")
    return sleep_duration
def main():
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(sleeping) for _ in range(20)]
        total_workload_time = 0
        max_workload_time = 0

        for idx, result in enumerate(results):
            sleep_duration = result.result()
            print(f"Task {idx + 1}: {sleep_duration} seconds")
            total_workload_time += sleep_duration
            max_workload_time = max(max_workload_time, sleep_duration)

        print(f"(Multithreading) Total workload time: {total_workload_time} seconds")
        print(f"(Multithreading) Max workload time: {max_workload_time} seconds")
        print(f"(Multithreading) Elapsed time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    main()


#---------------------------------------------------
#(optional) asyncio practice: Implement the multithreading task above using the asyncio approach.
import asyncio
print(f"\n\nAsyncio approach start:\n")

async def sleeping():
    sleep_duration = random.randint(1, 5)
    await asyncio.sleep(sleep_duration)
    print(f"Sleeping {sleep_duration} seconds")
    return sleep_duration

async def main():
    start_time = time.time()
    tasks = [sleeping() for _ in range(20)]
    results = await asyncio.gather(*tasks)
    total_workload_time = sum(results)
    max_workload_time = max(results)

    for idx, sleep_duration in enumerate(results):
        print(f"Task {idx + 1}: {sleep_duration} seconds")

    print(f"(Asyncio) Total workload time: {total_workload_time} seconds")
    print(f"(Asyncio) Max workload time: {max_workload_time} seconds")
    print(f"(Asyncio) Elapsed time: {time.time() - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())