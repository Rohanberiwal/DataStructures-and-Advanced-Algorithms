# Two-Pass Phase Concept in Array Traversal

## Overview
The two-pass phase concept is a common approach in array traversal problems. This method is particularly useful when calculating cumulative metrics or when previous results influence future results symmetrically. The concept involves two traversals (passes) over the array: one from left to right and one from right to left.

## Two-Pass Phase Concept

### First Pass (Left to Right)
- Traverse the array from the beginning to the end.
- Accumulate information or perform calculations using the current element and any relevant previous elements.
- Store the results in an intermediate array or structure.

### Second Pass (Right to Left)
- Traverse the array from the end to the beginning.
- Accumulate information or perform calculations using the current element and any relevant subsequent elements.
- Combine the results from this pass with the results from the first pass to get the final output.

## Example: Sum of Intervals Between Identical Elements

### Problem Statement
Given an array `arr` of integers, return an array `intervals` where `intervals[i]` is the sum of the absolute differences between the indices of `arr[i]` and each element in `arr` with the same value as `arr[i]`.

### Detailed Steps

#### First Pass (Left to Right)
- Use a dictionary to keep track of the last index of each value and the cumulative sum of intervals for each value up to the current index.
- For each element in the array, calculate the cumulative sum of intervals to all previous occurrences of the same value.
- Store this cumulative sum in a `left_distances` array.

#### Second Pass (Right to Left)
- Reset the dictionary to track the last index and cumulative sum for the second pass.
- Traverse the array from the end to the beginning, similarly calculating the cumulative sum of intervals to all subsequent occurrences of the same value.
- Store this cumulative sum in a `right_distances` array.

#### Combine Results
- For each element, the final interval sum is the sum of the values from `left_distances` and `right_distances`.

### Code Implementation

Here's the code that implements this approach:

```python
from typing import List

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        left_distances = [0] * n
        right_distances = [0] * n
        total_distances = [0] * n
        value_to_indices = {}

        # First pass: left to right
        for i in range(n):
            if arr[i] not in value_to_indices:
                value_to_indices[arr[i]] = []
            if value_to_indices[arr[i]]:
                left_distances[i] = left_distances[value_to_indices[arr[i]][-1]] + len(value_to_indices[arr[i]]) * (i - value_to_indices[arr[i]][-1])
            value_to_indices[arr[i]].append(i)
        
        # Reset value_to_indices for the second pass
        value_to_indices = {}

        # Second pass: right to left
        for i in range(n - 1, -1, -1):
            if arr[i] not in value_to_indices:
                value_to_indices[arr[i]] = []
            if value_to_indices[arr[i]]:
                right_distances[i] = right_distances[value_to_indices[arr[i]][-1]] + len(value_to_indices[arr[i]]) * (value_to_indices[arr[i]][-1] - i)
            value_to_indices[arr[i]].append(i)

        # Combine left and right distances
        for i in range(n):
            total_distances[i] = left_distances[i] + right_distances[i]

        return total_distances

# Example usage
solution = Solution()
arr = [2, 1, 3, 1, 2, 3, 3]
print(solution.getDistances(arr))  # Example output
