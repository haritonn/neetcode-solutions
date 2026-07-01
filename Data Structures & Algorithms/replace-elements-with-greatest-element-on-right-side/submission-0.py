class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        curr_max = self.findMax(0, arr)
        for i in range(len(arr)):
            if arr[i] == curr_max:
                curr_max = self.findMax(i, arr)
            res[i] = curr_max

        res[-1] = -1
        return res

    def findMax(self, idx: int, arr: list[int]) -> int:
        max_val = float('-inf')
        for i in range(idx+1, len(arr)):
            max_val = max(max_val, arr[i])

        return max_val