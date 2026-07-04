class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            num_to_find = target - numbers[left]
            if num_to_find == numbers[right]: return [left+1, right+1]
            if num_to_find > numbers[right]: left += 1
            else: right -= 1

        return [-1, -1]