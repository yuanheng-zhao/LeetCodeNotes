# Array, String
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        alpha_arr = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        shifts_each = [0 for _ in range(len(shifts))]
        total = 0
        for i in range(len(shifts) - 1, -1, -1):
            total += shifts[i]
            shifts_each[i] = total
        for i in range(len(shifts_each)):
            shifts_each[i] %= 26
        
        ans = ""
        for i in range(len(shifts_each)):
            c = alpha_arr[(alpha_arr.index(s[i]) + shifts_each[i]) % 26]
            ans += c

        return ans
