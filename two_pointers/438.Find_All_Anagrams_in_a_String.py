# Sliding Window, Hash
# TODO: re-organize folders like "sliding_window"

from typing import List, Dict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        def feasible(frequency: Dict[str, int]) -> bool:
            for k, v in frequency.items():
                if v != 0:
                    return False
            return True

        freq = {}
        for c in p:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        for i in range(len(p) - 1):
            if s[i] in freq:
                freq[s[i]] -= 1
        l = 0
        res = []
        for r in range(len(p) - 1, len(s)):
            if s[r] in freq:
                freq[s[r]] -= 1
            if feasible(freq):
                res.append(l)
            if s[l] in freq:
                freq[s[l]] += 1
            l += 1
        return res
