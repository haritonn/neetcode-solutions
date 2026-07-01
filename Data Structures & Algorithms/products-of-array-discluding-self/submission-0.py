class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return [math.prod(nums[:i]) * math.prod(nums[i+1:]) for i in range(len(nums))]
