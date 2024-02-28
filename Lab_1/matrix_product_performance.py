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

def matrix_matrix_product():
    n = 1000
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    C = np.zeros((n, n))
    CC = np.zeros((n, n))
    CCC = np.zeros((n, n))

    # Matrix-Matrix product with triple nested loops
    start_time = time.time()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] = C[i, j] + A[i, k] * B[k, j]
    loop_time = time.time() - start_time
    print(f"Result (nested loops): {C}")
    print(f"Time using triple nested loops: {loop_time} seconds")

    # Matrix-Matrix product with single loop and vectorization
    start_time = time.time()
    for i in range(n):  # Added this line to fix the issue
        CC[:, i] = np.dot(A, B[:, i])
    loop_vec_time = time.time() - start_time
    print(f"Result (vectorized loop): {CC}")
    print(f"Time using vectorization in loop: {loop_vec_time} seconds")

    # Matrix-Matrix product with full vectorization
    start_time = time.time()
    CCC = np.dot(A, B)
    vec_time = time.time() - start_time
    print(f"Result (fully vectorized): {CCC}")
    print(f"Time using full vectorization: {vec_time} seconds")

    # Compare results and measure speed-up
    print(f"Norm of difference (nested loops vs vectorized loop): {np.linalg.norm(C - CC)}")
    print(f"Norm of difference (nested loops vs fully vectorized): {np.linalg.norm(C - CCC)}")
    print(f"Speed-up (nested loops vs vectorized loop): {loop_time/loop_vec_time}")
    print(f"Speed-up (nested loops vs fully vectorized): {loop_time/vec_time}")
    print(f"Speed-up (vectorized loop vs fully vectorized): {loop_vec_time/vec_time}")

# Choose which function to run
def choose_function():
    print("Choose a function to run:")
    print("1. Dot Product")
    print("2. Matrix-Vector Product")
    print("3. Matrix-Matrix Product")

    choice = input("Enter 1, 2, or 3: ")
    
    if choice == '1':
        print("\nDot Product")
        for _ in range(10):
            dot_product()
    elif choice == '2':
        print("\nMatrix-Vector Product")
        for _ in range(10):
            matrix_vector_product()
    elif choice == '3':
        print("\nMatrix-Matrix Product")
        for _ in range(10):
            matrix_matrix_product()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

choose_function()
