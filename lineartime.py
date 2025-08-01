import time

def linear_time(n):
    print(f"\nO(n) with n = {n}")
    
    start = time.time()  # Start timing

    for i in range(n):
        _ = i * 2  # Dummy linear-time operation

    end = time.time()  # End timing
    
    print(f"Time taken: {end - start:.6f} seconds")

# Run with increasing input sizes
linear_time(10000)
linear_time(20000)
linear_time(30000)
