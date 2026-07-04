class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num > 0: break
            if i != 0 and num == nums[i-1]: continue
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = num + nums[left] + nums[right]
                if curr_sum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right: left += 1
                elif curr_sum > 0: right -= 1
                else: left += 1
        
        return res