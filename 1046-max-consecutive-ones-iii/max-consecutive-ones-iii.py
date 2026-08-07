class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        cnt = 0
        mx_lenght = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cnt += 1
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            mx_lenght = max(right - left  + 1,mx_lenght)
        return mx_lenght
                


       
