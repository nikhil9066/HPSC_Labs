import numpy as np

def apply_operation(chunk, op):
    if op == 'sum':
        return np.sum(chunk)
    elif op == 'average':
        return np.mean(chunk)
    elif op == 'min':
        return np.min(chunk)
    elif op == 'max':
        return np.max(chunk)
    else:
        raise ValueError("Unsupported operation")

def partition_cuboid(cuboid, nc):
    m, _, _ = cuboid.shape
    chunk_size = m // nc
    return [cuboid[i:i+chunk_size, :, :] for i in range(0, m, chunk_size)]

def mymapreduce(cuboid, nc, op):
    chunks = partition_cuboid(cuboid, nc)
    results = [apply_operation(chunk, op) for chunk in chunks]
    return np.sum(results)

# Test with random cuboid matrix
cuboid_matrix = np.random.randint(0, 100, size=(50, 100, 200))
nc_values = [2, 4, 8]
operations = ['sum', 'average', 'min', 'max']

for nc in nc_values:
    for op in operations:
        result = mymapreduce(cuboid_matrix, nc, op)
        print(f"nc={nc}, op={op}: result={result}")
