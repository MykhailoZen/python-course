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

    part_size = (range_end - range_start) // num_parts
    remainder = (range_end - range_start) % num_parts
    start = range_start
    end = range_start
    ranges_split = []

    for _ in range(num_parts):
        end += part_size + (1 if remainder > 0 else 0)
        ranges_split.append(range(start, end))
        start = end
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
    print("straight calc took", round(time.time() - start_time, 2), "seconds")
    print("straight calc result:", range_sum, "\n")

    start_time = time.time()
    ranges_split = split_range_into_n_parts(
        range_start,
        range_end + 1,
        num_parts)
    print("split list took", round(time.time() - start_time, 2), "seconds\n")

    start_time = time.time()
    result = main_task(ranges_split)
    print("split calc took", round(time.time() - start_time, 2), "seconds")
    print("split calc result:", result)
