import numpy as np
import time
import multiprocessing
from scipy import optimize
import matplotlib.pyplot as plt

def f(x):
    x = np.asarray(x)  # Convert to NumPy array
    return np.sin(3 * np.pi * np.cos(2 * np.pi * x) * np.sin(np.pi * x))


def find_root_newton(x):
    try:
        result = optimize.root_scalar(f, x0=x, method='newton')
        return result.root
    except ValueError:
        return None

def sequential_solver(x_values):
    roots = []
    for x in x_values:
        root = find_root_newton(x)
        if root is not None:
            roots.append(root)
    return roots

def parallel_worker(start_idx, end_idx, x_values, result_queue):
    try:
        roots = []
        for idx in range(start_idx, end_idx):
            root = find_root_newton(x_values[idx])
            if root is not None:
                roots.append(root)

        result_queue.put(roots)

    except Exception as e:
        print(f"Error in parallel_worker: {e}")
        result_queue.put([])  # Put an empty list to indicate an issue


def plot_roots_and_function(xx, f_values, roots, title):
    plt.figure(figsize=(12, 3))
    plt.plot(xx, f_values, '-k', linewidth=2, label="Function")
    plt.plot(roots, f(roots), 'o', markerfacecolor='r', label="Roots")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(-1, 1)
    plt.yticks([-1, 0, 1])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.legend()
    plt.savefig('MySavedPlot_PSV.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    a, b = -1, 1
    n = 1000
    x_values = np.linspace(a, b, n)

    # Sequential execution
    S_time = time.time()
    seq_roots = sequential_solver(x_values)
    E_time = time.time()
    seq_time = E_time - S_time

    # Parallel execution
    T_queue = multiprocessing.Queue()
    R_queue = multiprocessing.Queue()
    N_cores = multiprocessing.cpu_count()
    C_size = n // N_cores
    proc = []

    for core in range(N_cores):
        S_idx = core * C_size
        E_idx = S_idx + C_size
        process = multiprocessing.Process(target=parallel_worker, args=(S_idx, E_idx, x_values, R_queue))
        proc.append(process)
        process.start()

    for process in proc:
        process.join()

    parallel_roots = []
    while not R_queue.empty():
        parallel_roots.extend(R_queue.get())

    parallel_roots = np.unique(parallel_roots)
    P_time = time.time() - S_time
    S_up = seq_time / P_time
    effi = S_up / N_cores

    print(f"Speed up  : {S_up}")
    print(f"Efficiency  : {effi}")

    # Plot the function and roots
    xx = np.linspace(a, b, 1001)
    f_values = f(xx)

    # For sequential roots
    plot_roots_and_function(xx, f_values, seq_roots, "Sequential Roots")

    # For parallel roots
    plot_roots_and_function(xx, f_values, parallel_roots, "Parallel Roots")
