import matplotlib.pyplot as plt
import time

def generate_combinations(n):
    memo = {}
    def backtrack(index, ring_count, ding_count):
        if index == n:
            return [[]]  
        if (index, ring_count, ding_count) in memo:
            return memo[(index, ring_count, ding_count)]

        combinations = []
        for word in ["RING", "DING"]:
            if (word == "RING" and ring_count < 3) or (word == "DING" and ding_count < 3):
                new_ring_count = ring_count + 1 if word == "RING" else 0
                new_ding_count = ding_count + 1 if word == "DING" else 0
                sub_combinations = backtrack(index + 1, new_ring_count, new_ding_count)
                for sub_combination in sub_combinations:
                    combinations.append([word] + sub_combination)

        memo[(index, ring_count, ding_count)] = combinations
        return combinations

    return backtrack(0, 0, 0)

def calculate_max_sum(array, combination):
    max_sum = 0
    ring_count = 0

    for i, word in enumerate(combination):
        if word == "RING" and array[i] > 0:
            max_sum += array[i]
            ring_count += 1
        elif word == "DING" and array[i] < 0:
            max_sum += abs(array[i])
            ring_count = 0

        if ring_count > 3:
            return 0 
    return max_sum

# Generate runtimes
runtimes = []
for n in range(21):  # Vary the input size from 0 to 2000
    array = list(range(1, n+1))  # Generating a simple array as input
    start_time = time.time()  # Start measuring time
    extra = generate_combinations(n)
    max_sum = float('-inf')

    for i in extra:
        sum_i = calculate_max_sum(array, i)
        if sum_i > max_sum:
            max_sum = sum_i
            best_combination = i

    end_time = time.time()  # End measuring time
    runtime = end_time - start_time  # Calculate runtime
    runtimes.append(runtime)
    print(f"Finished calculating runtime for n={n}, runtime={runtime}")

# Plotting
plt.plot(range(21), runtimes)
plt.title('Runtime of Code vs Input Size')
plt.xlabel('Input Size (n)')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.show()
