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

def matrix_vector_product():
    n = 100
    A = np.random.rand(n, n)
    x = np.random.rand(n, 1)

    b = np.zeros((n, 1))
    bb = np.zeros((n, 1))
    bbb = np.zeros((n, 1))

    # Matrix-Vector product with nested loops
    start_time = time.time()
    for i in range(n):
        for j in range(n):
            b[i] = b[i] + A[i, j] * x[j]
    loop_time = time.time() - start_time
    print(f"Result: {b}")
    print(f"Time using nested loops: {loop_time} seconds")

    # Matrix-Vector product with single loop and vectorization
    start_time = time.time()
    for i in range(n):
        bb[i] = np.dot(A[i, :], x)
    loop_vec_time = time.time() - start_time
    print(f"Result (vectorized loop): {bb}")
    print(f"Time using vectorization in loop: {loop_vec_time} seconds")

    # Matrix-Vector product with full vectorization
    start_time = time.time()
    bbb = np.dot(A, x)
    vec_time = time.time() - start_time
    print(f"Result (fully vectorized): {bbb}")
    print(f"Time using full vectorization: {vec_time} seconds")

    # Compare results and measure speed-up
    print(f"Norm of difference (nested loops vs vectorized loop): {np.linalg.norm(b - bb)}")
    print(f"Norm of difference (nested loops vs fully vectorized): {np.linalg.norm(b - bbb)}")
    print(f"Speed-up (nested loops vs vectorized loop): {loop_time/loop_vec_time}")
    print(f"Speed-up (nested loops vs fully vectorized): {loop_time/vec_time}")
    print(f"Speed-up (vectorized loop vs fully vectorized): {loop_vec_time/vec_time}")