class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        a = []
        s_t = set("qwertyuiopQWERTYUIOP")
        s = set("asdfghjklASDFGHJKL")
        t = set("zxcvbnmZXCVBNM")
        for i in words:
            letters = set(i)
            if letters<=s_t or letters<=s or letters<=t:
                a.append(i)
        return a