import numpy as np
import time
import multiprocessing
from joblib import Parallel, delayed

def calculate_partial_integral(process_id, total_processes, integrand, lower_bound_x, upper_bound_x, lower_bound_y, upper_bound_y, points_per_dimension=100):
    segment_width_x = (upper_bound_x - lower_bound_x) / total_processes
    segment_width_y = (upper_bound_y - lower_bound_y) / total_processes
    segment_x_start = lower_bound_x + process_id * segment_width_x
    segment_x_end = lower_bound_x + (process_id + 1) * segment_width_x
    segment_y = [lower_bound_y, upper_bound_y]
    segment_integral = 0.0
    for x in np.linspace(segment_x_start, segment_x_end, points_per_dimension):
        for y in np.linspace(segment_y[0], segment_y[1], points_per_dimension):
            segment_integral += integrand(x, y) * segment_width_x * segment_width_y
    return segment_integral

def compute_double_integral_parallel(integrand, lower_x, upper_x, lower_y, upper_y, worker_count=2, integration_points=100):
    process_pool = multiprocessing.Pool(processes=worker_count)
    task_args = [(proc_id, worker_count, integrand, lower_x, upper_x, lower_y, upper_y, integration_points) for proc_id in range(worker_count)]
    partial_integrals = process_pool.starmap(calculate_partial_integral, task_args)
    process_pool.close()
    process_pool.join()
    return sum(partial_integrals)

def compute_double_integral_serial(integrand, lower_x, upper_x, lower_y, upper_y, integration_points=100):
    total_integral = 0
    for x in np.linspace(lower_x, upper_x, integration_points):
        for y in np.linspace(lower_y, upper_y, integration_points):
            total_integral += integrand(x, y) * (upper_x - lower_x) / integration_points * (upper_y - lower_y) / integration_points
    return total_integral

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == '__main__':
    x_lower_bound, x_upper_bound = 0.0, 1.0
    y_lower_bound, y_upper_bound = 0.0, 1.0
    parallel_workers = 4
    sampling_points = 100

    # Parallel double integral computation
    computed_integral_parallel, parallel_duration = measure_execution_time(
        compute_double_integral_parallel, np.multiply, x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound,
        parallel_workers, sampling_points
    )

    # Serial double integral computation
    computed_integral_serial, serial_duration = measure_execution_time(
        compute_double_integral_serial, np.multiply, x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound, sampling_points
    )

    # Calculate performance metrics
    performance_speedup = serial_duration / parallel_duration
    efficiency = performance_speedup / parallel_workers

    # Output the results
    print('Calculated double integral value (Parallel):', computed_integral_parallel)
    print('Parallel computation time:', parallel_duration)
    print('Serial computation time:', serial_duration)
    print('Performance Speedup:', performance_speedup)
    print('Efficiency:', efficiency)

if __name__ == '__main__':
    x_lower_bound, x_upper_bound = 0.0, 1.0
    y_lower_bound, y_upper_bound = 0.0, 1.0
    num_parallel_workers = 4
    sampling_points = 100
    num_iterations = 10

    for iteration in range(num_iterations):
        print(f"\nIteration {iteration + 1}")

        # Parallel double integral computation
        parallel_integral_result, parallel_duration = measure_execution_time(
            compute_double_integral_parallel, np.multiply, x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound,
            num_parallel_workers, sampling_points
        )

        # Serial double integral computation
        serial_integral_result, serial_duration = measure_execution_time(
            compute_double_integral_serial, np.multiply, x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound, sampling_points
        )

        # Calculate performance metrics
        performance_speedup = serial_duration / parallel_duration
        efficiency = performance_speedup / num_parallel_workers

        # Output the results
        print('Calculated double integral value (Parallel):', parallel_integral_result)
        print('Parallel computation time:', parallel_duration)
        print('Serial computation time:', serial_duration)
        print('Performance Speedup:', performance_speedup)
        print('Efficiency:', efficiency)



"""# **Tripple Integral**


"""

import numpy as np
import multiprocessing
import time

def f(x, y, z):
    # Define the specific function to integrate here
    return x * y * z

def calculate_partial_triple_integral(process_id, total_processes, integrand, lower_bound_x, upper_bound_x, lower_bound_y, upper_bound_y, lower_bound_z, upper_bound_z, points_per_dimension=100):
    segment_width_x = (upper_bound_x - lower_bound_x) / total_processes
    segment_width_y = (upper_bound_y - lower_bound_y) / total_processes
    segment_width_z = (upper_bound_z - lower_bound_z) / total_processes

    segment_start_x = lower_bound_x + process_id * segment_width_x
    segment_end_x = lower_bound_x + (process_id + 1) * segment_width_x

    segment_y_range = [lower_bound_y, upper_bound_y]
    segment_z_range = [lower_bound_z, upper_bound_z]

    segment_integral = 0.0

    for x in np.linspace(segment_start_x, segment_end_x, points_per_dimension):
        for y in np.linspace(segment_y_range[0], segment_y_range[1], points_per_dimension):
            for z in np.linspace(segment_z_range[0], segment_z_range[1], points_per_dimension):
                segment_integral += integrand(x, y, z) * segment_width_x * segment_width_y * segment_width_z

    return segment_integral

def compute_triple_integral_parallel(integrand, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z, num_workers=2, integration_points=100):
    process_pool = multiprocessing.Pool(processes=num_workers)
    task_args = [
        (proc_id, num_workers, integrand, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z, integration_points)
        for proc_id in range(num_workers)
    ]
    partial_integrals = process_pool.starmap(calculate_partial_triple_integral, task_args)
    process_pool.close()
    process_pool.join()
    return sum(partial_integrals)

if __name__ == '__main__':
    x_lower_bound, x_upper_bound = 0.0, 1.0
    y_lower_bound, y_upper_bound = 0.0, 2.0
    z_lower_bound, z_upper_bound = 0.0, 3.0

    num_parallel_workers = 4
    sampling_points = 100
    num_iterations = 10

    for iteration in range(num_iterations):
        print(f"\nIteration {iteration + 1}")

        # Timing the parallel triple integral computation
        parallel_start = time.time()
        computed_integral_parallel = compute_triple_integral_parallel(f, x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound, z_lower_bound, z_upper_bound, num_parallel_workers, sampling_points)
        parallel_end = time.time()
        parallel_duration = parallel_end - parallel_start

        # Timing the serial triple integral computation
        serial_start = time.time()
        computed_integral_serial = calculate_partial_triple_integral(0, 1, f, x_lower_bound, x_upper_bound, y_lower_bound, y_upper_bound, z_lower_bound, z_upper_bound, sampling_points)
        serial_end = time.time()
        serial_duration = serial_end - serial_start

        # Calculating performance metrics
        performance_speedup = serial_duration / parallel_duration
        efficiency = performance_speedup / num_parallel_workers

        # Output the results
        print('Calculated triple integral value (Parallel):', computed_integral_parallel)
        print('Parallel computation time:', parallel_duration)
        print('Serial computation time:', serial_duration)
        print('Performance Speedup:', performance_speedup)
        print('Efficiency:', efficiency)