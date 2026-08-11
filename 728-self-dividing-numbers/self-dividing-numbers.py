class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst =[]
        for i in range(left,right+1):
            cnt=0
            for j in str(i):
                if int(j)!=0:
                    if i%int(j)==0:
                        cnt+=1
            if cnt==len(str(i)):
                lst.append(i)

        return lst
