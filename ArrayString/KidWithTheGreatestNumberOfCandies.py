class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                candies[i] = True
            else:
                candies[i] = False
        return candies

        # Alternative 
        # return [(i + extraCandies >= greatest) for i in candies]