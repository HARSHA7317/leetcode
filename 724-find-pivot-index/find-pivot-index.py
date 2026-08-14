class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        rs = 0
        for i in nums:
            rs += i
            prefix_sum.append(rs)
        for i in range(len(nums)):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[len(nums)]-prefix_sum[i+1]
            if left_sum == right_sum:
                return i
        return -1
            
        