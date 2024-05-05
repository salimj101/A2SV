# User function Template for python3

class Solution:
    # def select(self, arr, i):
    # code here

    def selectionSort(self, arr, n):
        # code here
        n = len(arr)
        for i in range(n):

            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
