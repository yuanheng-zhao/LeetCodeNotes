class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        min_len = len(s) + 1
        l = 0
        freq = {}
        for c in t:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
                
        cnt = 0
        for r, c in enumerate(s):
            if c in freq:
                freq[c] -= 1
                if freq[c] >= 0:
                    cnt += 1
            while cnt == len(t):
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    res = s[l:r+1]
                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:      
                        cnt -= 1
                l += 1
        
        return res
