class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # approach :sort+two pointer(two sum approach)
        result=set()
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                   result.add((nums[i],nums[left],nums[right]))
                   left+=1
                   right-=1
                elif sum>0:
                    right-=1
                else:
                    left+=1
        return list(result)
