class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = float("-inf")
        while left < right:
            lbar, rbar = heights[left], heights[right]
            curr_prod = min(lbar, rbar) * (right - left)
            res = max(curr_prod, res)

            if lbar > rbar: right -= 1
            else: left += 1

        return res

