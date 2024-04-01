import multiprocessing
import concurrent.futures
import time

range_start = 1
range_end = 2**30
num_parts = multiprocessing.cpu_count()

def calculate_range_sum(range_start, range_end):

    res_1 = sum(range(range_start, range_end + 1))


    return res_1

def split_range_into_n_parts(range_start, range_end, num_parts):
    #start_time = time.time()
    part_size = (range_end - range_start) // num_parts
    remainder = (range_end - range_start) % num_parts

    # Initialize the start and end of the current part
    start = range_start
    end = range_start

    # Generate the ranges for each part
    ranges_split = []
    for _ in range(num_parts):
        # Adjust the end of the part based on the remainder
        end += part_size + (1 if remainder > 0 else 0)
        # Add the range to the list
        ranges_split.append(range(start, end))
        # Update the start for the next part
        start = end
        # Decrease the remainder
        remainder -= 1

    return ranges_split

def process_data(item):
    return sum(item)

def main_task(data_x):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_parts) as executor:
        futures = [executor.submit(process_data, item) for item in data_x]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return sum(results)

if __name__ == "__main__":
    start_time = time.time()
    range_sum = calculate_range_sum(range_start, range_end)
    print("calculate_range_sum time", time.time() - start_time, "seconds")
    print("calculate_range_sum sum", range_sum)

    start_time = time.time()
    ranges_split = split_range_into_n_parts(range_start, range_end +1, num_parts)
    #print(ranges_split)
    print("split list took", time.time() - start_time, "seconds")

    start_time = time.time()

    result = main_task(ranges_split)
    print("Result:", result)
    print("split calc took", time.time() - start_time, "seconds")