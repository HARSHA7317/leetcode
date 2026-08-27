class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxones = 0
        for i in nums:
            if i == 1:
                count+=1
            else:
                maxones = max(count,maxones)
                count = 0
        return max(count,maxones)
