class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        print(s)
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]: return False
            left += 1
            right -= 1

        return True