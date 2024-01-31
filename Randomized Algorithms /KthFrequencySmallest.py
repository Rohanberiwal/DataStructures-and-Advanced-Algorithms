##Does the binary search for the elment in the Logn and find the smallest element freqency wise
    def singleNonDuplicate(self, arr: List[int]) -> int:
        i = 0
        j = len(arr) - 1
        while i < j:
            m = (i+j) // 2
            if m < j and arr[m] == arr[m+1]:
                m = m + 1
            if arr[m] != arr[m-1] and arr[m] != arr[m+1]:
                return arr[m]
            elif abs(m-i) % 2 == 0:
                j = m - 1
            else:
                i = m + 1 
        return arr[i]
