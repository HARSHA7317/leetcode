class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp,result = word,0
        while temp in sequence:
            result+=1
            temp+=word
        return result
        