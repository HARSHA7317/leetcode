class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        for i in p:
            d1[i] = d1.get(i,0) + 1
        left = 0
        k = len(p)
        ans = []
        d2 = {}
        for i in range(len(s)):
            d2[s[i]] = d2.get(s[i],0) + 1
            if i >= k -1:
                if d1 == d2:
                    ans.append(left)
                d2[s[left]] -= 1
                if d2[s[left]] == 0:
                    d2.pop(s[left])
                left += 1
        return ans
        