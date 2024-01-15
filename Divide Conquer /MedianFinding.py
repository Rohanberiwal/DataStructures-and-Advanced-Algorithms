###Taken from a LLM :
###Balance the partation function :

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

### Select function :
def quick_select(arr, low, high, k):
    if low < high:
        pi = partition(arr, low, high)

        if pi == k:
            return arr[pi]
        elif pi < k:
            return quick_select(arr, pi + 1, high, k)
        else:
            return quick_select(arr, low, pi - 1, k)

def find_median(arr):
    n = len(arr)
    if n % 2 == 0:
        # For even-sized arrays, return the average of the two middle elements
        middle1 = quick_select(arr, 0, n - 1, n // 2 - 1)
        middle2 = quick_select(arr, 0, n - 1, n // 2)
        return (middle1 + middle2) / 2
    else: 
        # For odd-sized arrays, return the middle element
        return quick_select(arr, 0, n - 1, n // 2)
