class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str = ""
        a=len(word1)
        b=len(word2)
        c=min(a,b)
        d=max(a,b)
        for i in range(c):
            str+=word1[i]+word2[i]
        if a>=b:
            str+=word1[c:]
        elif a<=b:
            str+=word2[c:]
        return str

           

                
        