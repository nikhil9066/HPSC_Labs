import time
import multiprocessing

def time_consuming_fun(duration):
    time.sleep(duration)

def run_experiment(n):
    start_time = time.time()
    for _ in range(n):
        time_consuming_fun(1 + 4 * (time.time() % 5))
    serial_time = time.time() - start_time

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(time_consuming_fun, [1 + 4 * (time.time() % 5) for _ in range(n)])
    parallel_time = time.time() - start_time

    speedup = serial_time / parallel_time
    efficiency = speedup / multiprocessing.cpu_count()
    return serial_time, parallel_time, speedup, efficiency

n_small = 10
n_medium = 100
n_large = 1000
print("Small")
serial_time_small, parallel_time_small, speedup_small, efficiency_small = run_experiment(n_small)
serial_time_medium, parallel_time_medium, speedup_medium, efficiency_medium = run_experiment(n_medium)
serial_time_large, parallel_time_large, speedup_large, efficiency_large = run_experiment(n_large)

print(f"Results for n = {n_small}:")
print(f"Serial Time: {serial_time_small} seconds")
print(f"Parallel Time: {parallel_time_small} seconds")
print(f"Speedup: {speedup_small}")
print(f"Efficiency: {efficiency_small}\n")

print(f"Results for n = {n_medium}:")
print(f"Serial Time: {serial_time_medium} seconds")
print(f"Parallel Time: {parallel_time_medium} seconds")
print(f"Speedup: {speedup_medium}")
print(f"Efficiency: {efficiency_medium}\n")

print(f"Results for n = {n_large}:")
print(f"Serial Time: {serial_time_large} seconds")
print(f"Parallel Time: {parallel_time_large} seconds")
print(f"Speedup: {speedup_large}")
print(f"Efficiency: {efficiency_large}")
