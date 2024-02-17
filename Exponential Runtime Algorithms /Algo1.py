##from itertools import combination 

def generate_combinations(n):
    memo = {}

    def backtrack(combination, ring_count, ding_count):
        if len(combination) == n:
            return [tuple(combination)]

        if (tuple(combination), ring_count, ding_count) in memo:
            return memo[(tuple(combination), ring_count, ding_count)]

        listextra = []
        for word in ["RING", "DING"]:
            if (word == "RING" and ring_count < 3) or (word == "DING" and ding_count < 3):
                nums  = combination + [word]
                new_ring_count = ring_count + 1 if word == "RING" else 0
                new_ding_count = ding_count + 1 if word == "DING" else 0
                listextra.extend(backtrack(nums, new_ring_count, new_ding_count))

        memo[(tuple(combination), ring_count, ding_count)] = listextra
        return listextra

    return backtrack([], 0, 0)

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

if _name_ == "_main_":
    array = []
    n = int(input("Enter the size of the array: "))
    for i in range(n):
        array.append(int(input("Enter the element: ")))

    extra = generate_combinations(n)
    max_sums = []

    for i in extra :
        max_sums.append(calculate_max_sum(array, i))
        print("Combination:", i)

  #  print("Maximum sum for each combination:", max_sums)
    print("Maximum chickens earned by Mr. Fox:", max(max_sums))

    extra = []
    for i in range(n):
        if array[i] > 0:
            extra.append(array[i])
        elif array[i] < 0:
            extra.append(abs(array[i]))

   # print("List of extra variables:", extra)
