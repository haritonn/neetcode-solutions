class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c not in brackets_map.values():
                if not stack or stack.pop() != brackets_map[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0