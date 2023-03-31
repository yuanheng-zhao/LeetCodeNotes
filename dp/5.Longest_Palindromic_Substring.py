# DP
class Solution:

    # Time Complexity: O(n^2), Space Complexity: O(n^2)
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s
    
        res = ""
        # dp[i][j] represents whether substring s[i:j+1] is a palindrom
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]

        return res

    # 中心扩散法 Time Complexity: O(n^2), Space Complexity: O(1)
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s
    
        res = ""
        for i in range(len(s)):
            # condition 1: length is odd; center is a single char
            l = r = i
            curr = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                l -= 1
                r += 1
            if len(curr) > len(res):
                res = curr
            # condition 2: length is even; center is two chars
            l, r = i, i + 1
            curr = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                l -= 1
                r += 1
            if len(curr) > len(res):
                res = curr

        return res
