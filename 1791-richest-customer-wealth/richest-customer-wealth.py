class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lst = []
        mx=0
        for i in accounts:
            s=0
            for j in i:
                s+=j
            mx=max(mx,s)
        return mx


