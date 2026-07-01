class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod, zero_counter = 1, 0
        res = [0] * len(nums)
        for num in nums:
            if num:
                prod *= num
            else:
                zero_counter += 1

        if zero_counter > 1:
            return res

        for i, num in enumerate(nums):
            if zero_counter:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num

        return res
