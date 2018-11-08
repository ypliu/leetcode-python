class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        if not ratings or 0 == len(ratings):
            return 0
        elif 1 == len(ratings):
            return 1
        return self.candyAssignLinearSpace(ratings)

    def candyAssignLinearSpace(self, ratings):
        candies = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)

    #def candyAssignConstSpace(self, ratings):

# debus
s = Solution()
print s.candy([1,0,2])
print s.candy([1,2,2])
print s.candy([1,3,2,2,1])
