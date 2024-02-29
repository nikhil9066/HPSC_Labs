import concurrent.futures
import time

def simulate_small_iteration(iterations):
    for _ in range(iterations):
        time.sleep(0.01)

def simulate_medium_iteration(iterations):
    for _ in range(iterations):
        time.sleep(0.01)

def simulate_large_iteration(iterations):
    for _ in range(iterations):
        time.sleep(0.01)

def run_parallel_iterations(num_iterations, num_threads, simulate_function):
    start_time_single = time.time()
    simulate_function(1)
    single_iteration_duration = time.time() - start_time_single

    start_time_parallel = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(simulate_function, 1) for _ in range(num_iterations)]
    concurrent.futures.wait(futures)

    parallel_iterations_duration = time.time() - start_time_parallel

    speed_up = single_iteration_duration / parallel_iterations_duration
    efficiency = speed_up / num_iterations

    return single_iteration_duration, parallel_iterations_duration, speed_up, efficiency

def run_all_iterations(iteration_data):
    for choice, data in iteration_data.items():
        print(f"\nRunning {data['function'].__name__} iteration:")
        simulate_function = data["function"]
        num_iterations = data["num"]

        num_threads = 4

        single_iteration_duration, parallel_iterations_duration, speed_up, efficiency = run_parallel_iterations(num_iterations, num_threads, simulate_function)

        print(f"Elapsed time for a single iteration: {single_iteration_duration:.3f} seconds")
        print(f"Elapsed time for parallel iterations: {parallel_iterations_duration:.3f} seconds")
        print(f"Speed up: {speed_up:.2f}")
        print(f"Efficiency: {efficiency:.2f}")

if __name__ == "__main__":
    iteration_data = {
        "1": {"function": simulate_small_iteration, "num": 10},
        "2": {"function": simulate_medium_iteration, "num": 100},
        "3": {"function": simulate_large_iteration, "num": 500},
    }

    run_all_iterations(iteration_data)
