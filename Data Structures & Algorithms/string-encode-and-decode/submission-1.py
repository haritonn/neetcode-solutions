class Solution:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(s)}@{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res, i = [], 0

        while i < len(s):
            j = s.find('@', i)
            length = int(s[i:j])

            res.append(s[j+1:j+length+1])
            i = j + 1 + length

        return res
