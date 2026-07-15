class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for st in strs:
                string+=str(len(st))+"#"+st
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            j += 1
            res.append(s[j : j + length])

            i = j + length
        return res