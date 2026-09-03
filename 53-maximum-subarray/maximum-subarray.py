class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = 0
        best = nums[0]
        for num in nums:
            mx += num
            best = max(best,mx)

            if mx<0:
                mx = 0
        return best