# Backtracking
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def bt(output: List[int], choices: List[int], res: List[int]) -> None:
            if len(choices) == 0:
                res.append(output.copy())
                return
            for i, choice in enumerate(choices):
                output.append(choice)
                bt(output, choices[:i] + choices[i+1:], res)
                output.pop()
        
        res = []
        bt([], nums, res)
        return res
    
    # Not recording each choice made along a path, instead, use an array 
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def bt(nums: List[int], output: List[int], used: List[int], res: List[int]) -> None:
            if len(output) == len(nums):
                res.append(output.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                output.append(nums[i])
                bt(nums, output, used, res)
                output.pop()
                used[i] = False

        res = []
        used = [False for _ in range(len(nums))]
        bt(nums, [], used, res)
        return res
