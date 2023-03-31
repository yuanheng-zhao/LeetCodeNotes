# Hash, Array, Design
import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.htable = {}  # val -> index of val in arr

    def insert(self, val: int) -> bool:
        if val in self.htable:
            return False
        self.arr.append(val)
        self.htable[val] = len(self.arr) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.htable:
            return False
        idx = self.htable[val]
        if idx == len(self.arr) - 1:
            self.arr.pop()
            self.htable.pop(val)
        else:
            last_val = self.arr[-1]
            self.arr[idx] = last_val
            self.arr.pop()
            self.htable[last_val] = idx
            self.htable.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.arr)  # Is this a 偷手?


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
