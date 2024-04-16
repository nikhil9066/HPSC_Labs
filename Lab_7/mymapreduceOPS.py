import numpy as np

def map_operation(matrix_chunk, op):
    if op == 'sum':
        return np.sum(matrix_chunk)
    elif op == 'average':
        return np.mean(matrix_chunk)
    elif op == 'min':
        return np.min(matrix_chunk)
    elif op == 'max':
        return np.max(matrix_chunk)
    else:
        raise ValueError("Unsupported operation")

def mymapreduce(matrix, nc, op):
    m, n = matrix.shape
    chunk_size = m // nc
    chunk_indices = [i * chunk_size for i in range(nc)]
    chunks = [matrix[i:i+chunk_size, :] for i in chunk_indices]
    results = [map_operation(chunk, op) for chunk in chunks]
    return np.sum(results)

# Test with random matrix
matrix = np.random.randint(0, 100, size=(800, 1000))
nc_values = [2, 4, 8]
operations = ['sum', 'average', 'min', 'max']

for nc in nc_values:
    for op in operations:
        result = mymapreduce(matrix, nc, op)
        print(f"nc={nc}, op={op}: result={result}")
