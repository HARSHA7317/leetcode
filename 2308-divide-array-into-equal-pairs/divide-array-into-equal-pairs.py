from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        a = len(nums) // 2
        f = Counter(nums)
        for i in f.values():
            if i % 2 != 0:
                return False
        return True        
     