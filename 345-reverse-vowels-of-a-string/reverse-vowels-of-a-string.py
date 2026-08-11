def is_vowel(ch):
    return ch in "aeiouAEIOU"
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        s=list(s)
        while left<right:
            if is_vowel(s[left]) and is_vowel(s[right]):
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            elif is_vowel(s[right]):
                left += 1
            elif is_vowel(s[left]):
                right -= 1
            else:
                left+=1
                right-=1
        return "".join(s)
        

        