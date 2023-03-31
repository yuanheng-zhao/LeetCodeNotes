# Two Pointers, Array

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        res = 0
        for word in words:
            i_word = 0
            stretchy = True  # assume true
            for i_s in range(len(s)):
                if i_word < len(word) and s[i_s] == word[i_word]:
                    i_word += 1
                elif i_s > 0 and i_s < len(s) - 1 and s[i_s-1] == s[i_s] == s[i_s+1]:
                    pass
                elif i_s > 1 and s[i_s-2] == s[i_s-1] == s[i_s]:
                    pass
                else:
                    stretchy = False
                    break
            if i_word != len(word):  # word still has un-processed char(s) 
                stretchy = False
            if stretchy:
                res += 1
        return res
