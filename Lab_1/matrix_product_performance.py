import numpy as np
import time

def dot_product():
    n = 10000
    a = np.random.rand(n, 1)
    b = np.random.rand(n, 1)

    c = 0
    # Dot product with for-loop
    start_time = time.time()
    for i in range(n):
        c = c + a[i] * b[i]
    loop_time = time.time() - start_time
    print(f"Result: {c}")
    print(f"Time using for-loop: {loop_time} seconds")

    # Dot product with vectorization
    start_time = time.time()
    cc = np.dot(a.flatten(), b.flatten())
    vec_time = time.time() - start_time
    print(f"Result (vectorized): {cc}")
    print(f"Time using vectorization: {vec_time} seconds")
    
    # Compare results and measure speed-up
    print(f"Norm of difference: {np.linalg.norm(c - cc)}")
    print(f"Speed-up: {loop_time/vec_time}")

dot_product()