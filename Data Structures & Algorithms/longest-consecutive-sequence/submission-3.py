class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        length = 0
        res = float("-inf")
        for num in nums_set:
            curr_num = num
            while curr_num in nums_set:
                print(curr_num)
                length += 1
                curr_num += 1
            res = max(length, res)
            length = 0

        return res