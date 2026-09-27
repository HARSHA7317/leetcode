class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    found = -1
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > i:
                            found = nums2[k]
                            break
                    ans.append(found)
        return ans