import numpy as np

def mymapreduce(v, nc, op):
    # Map part
    chunk_size = len(v) // nc
    chunks = [v[i:i+chunk_size] for i in range(0, len(v), chunk_size)]
    
    # Apply operation to each partition
    if op == 'sum':
        results = [np.sum(chunk) for chunk in chunks]
    elif op == 'average':
        results = [np.mean(chunk) for chunk in chunks]
    elif op == 'min':
        results = [np.min(chunk) for chunk in chunks]
    elif op == 'max':
        results = [np.max(chunk) for chunk in chunks]
    else:
        raise ValueError("Unsupported operation")
    
    # Reduce part
    final_result = np.sum(results)
    
    return final_result

# Test with random vector
v = np.random.randint(0, 100, 1000)
nc_values = [2, 4, 8]
operations = ['sum', 'average', 'min', 'max']

for nc in nc_values:
    for op in operations:
        result = mymapreduce(v, nc, op)
        print(f"nc={nc}, op={op}: result={result}")
