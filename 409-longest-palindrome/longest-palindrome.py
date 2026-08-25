class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            d[i]=d.get(i,0)+1
        ans = 0
        H_odd = False
        for count in d.values():
            ans+=(count//2)*2
            if count%2==1:
                H_odd=True
        if H_odd:
            ans += 1
        return ans
            
        