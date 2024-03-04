import concurrent.futures
import time

def simulate_task(iterations):
    for j in range(iterations):
        time.sleep(0.01)

def run_parallel_tasks(num_tasks, num_threads):
    start_time_single_task = time.time()
    simulate_task(1)
    elapsed_time_single_task = time.time() - start_time_single_task

    start_time_parallel_tasks = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(simulate_task, 1) for i in range(num_tasks)]
    concurrent.futures.wait(futures)
    elapsed_time_parallel_tasks = time.time() - start_time_parallel_tasks

    speedup = elapsed_time_single_task / elapsed_time_parallel_tasks
    efficiency = speedup / num_tasks

    print("\n")
    print(f"Number of task: ", num_tasks)
    print(f"Elapsed time for a single task: {elapsed_time_single_task:.3f} seconds")
    print(f"Elapsed time for parallel tasks: {elapsed_time_parallel_tasks:.3f} seconds")
    print(f"Speed up: {speedup:.2f}")
    print(f"Efficiency: {efficiency:.2f}")

if __name__ == "__main__":
    # Parallel tasks with 10 iterations and 4 threads
    run_parallel_tasks(10, 4)
    run_parallel_tasks(100, 4)
    run_parallel_tasks(1000, 4)