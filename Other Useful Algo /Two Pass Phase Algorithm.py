class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        left_distances = [0] * n
        right_distances = [0] * n
        total_distances = [0] * n
        prev_index = {}

        # First pass: left to right
        for i in range(n):
            if arr[i] in prev_index:
                left_distances[i] = left_distances[prev_index[arr[i]]] + (i - prev_index[arr[i]])
            else:
                left_distances[i] = 0
            prev_index[arr[i]] = i
        
        # Reset prev_index for the second pass
        prev_index = {}

        # Second pass: right to left
        for i in range(n - 1, -1, -1):
            if arr[i] in prev_index:
                right_distances[i] = right_distances[prev_index[arr[i]]] + (prev_index[arr[i]] - i)
            else:
                right_distances[i] = 0
            prev_index[arr[i]] = i

        # Combine left and right distances
        for i in range(n):
            total_distances[i] = left_distances[i] + right_distances[i]

        return total_distances
