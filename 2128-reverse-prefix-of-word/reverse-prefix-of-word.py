class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        a=[]
        n =len(word)-1
        for i in range(len(word)):
            a.append(word[i])
            if word[i]==ch:
                a.reverse()
                c=i
                break
            if ch not in word:
                return word
        b = "".join(a)
        e=word[c+1:]
        
        return b+e

