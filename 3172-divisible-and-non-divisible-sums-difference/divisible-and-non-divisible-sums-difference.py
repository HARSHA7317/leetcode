class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        not_div=[]
        div_=[]
        for i in range(1,n+1):
            if i%m==0:
                not_div.append(i)
            else:
                div_.append(i)
        sum1=sum(not_div)
        sum2=sum(div_)
        return sum2-sum1
