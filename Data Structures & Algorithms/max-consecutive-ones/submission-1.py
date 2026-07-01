class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter, res = 0, 0
        for num in nums:
            if num == 1: 
                counter += 1
                res = max(counter, res)
            else: counter = 0

        return res