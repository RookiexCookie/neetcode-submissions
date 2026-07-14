class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            count = bytearray(26) 
            for ch in word:
                count[ord(ch) - 97] += 1
            key = bytes(count)
            group.setdefault(key, []).append(word)
        return list(group.values())