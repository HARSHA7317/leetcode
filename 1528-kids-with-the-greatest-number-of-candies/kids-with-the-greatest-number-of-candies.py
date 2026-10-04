class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        result = []
        
        maximum = max(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
        
        return result