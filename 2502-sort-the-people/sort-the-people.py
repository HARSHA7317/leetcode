class Solution:
    def sortPeople(self, names, heights):
        d = list(zip(names, heights))
        d.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in d]