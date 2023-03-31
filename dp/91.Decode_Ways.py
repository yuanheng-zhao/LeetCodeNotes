# DP
class Solution:

    # sdiofh4389bdfnognpb
    def numDecodings(self, s: str) -> int:
        
        dp = [0 for _ in range(len(s))]
        dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            # since s contains only digits, s[i] is in {0, 1, 2, ..., 9}

            if s[i] == '0' and '1' <= s[i-1] <= '2':
                if i >= 2:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1]
            elif s[i] != '0':

                dp[i] = dp[i-1]

                if s[i-1] != '0' and 10 <= int(s[i-1:i+1]) <= 26:
                    if i >= 2:
                        dp[i] += dp[i-2]
                    else:
                        dp[i] += 1

        # print(dp)
        return dp[-1]
    

    def numDecodings(self, s: str) -> int:

        """
        e.g. 
        s = "1402"
        dp[5] = [x0, x1, x2, x3, x4]
        dp[0] = x0 => ways to decode ""
        dp[1] = x1 => ways to decode "1"  s[0:1]
        dp[2] = x2 => ways to decode "14" s[0:2]
        dp[3] = x3 => ways to decode "140" 
        dp[4] = x4 => ways to decode "1402" 
        """

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
