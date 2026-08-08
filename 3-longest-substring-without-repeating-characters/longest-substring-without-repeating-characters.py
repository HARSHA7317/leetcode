class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d2=set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in d2:
                d2.remove(s[left])
                left += 1
            d2.add(s[right])
            ans = max(ans,right - left + 1)
        return ans            
                


            

        


