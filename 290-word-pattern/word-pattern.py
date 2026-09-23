class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool: 
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = {}
        d2 = {}
        for i in range(len(pattern)):   
            letter = pattern[i]
            word = words[i]
            if letter in d and d[letter] != word:
                return False
            if word in d2 and d2[word] != letter:
                return False
            d[letter] = word
            d2[word] = letter
        return True