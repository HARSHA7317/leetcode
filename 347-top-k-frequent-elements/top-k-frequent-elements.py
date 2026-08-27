class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums :
            if i in d.keys():
                d[i]+= 1
            else:
                d[i]=1
        a=sorted(d.items(),key=lambda t:t[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(a[i][0])
        return ans
           
            
           
    
