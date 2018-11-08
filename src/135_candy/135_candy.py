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
        # return self.candyAssignLinearSpace(ratings)
        return self.candyAssignConstSpace(ratings)

    def candyAssignLinearSpace(self, ratings):
        candies = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)

    def candyAssignConstSpace(self, ratings):
        candies = 0
        ups = downs = 0
        pre_slope = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                cur_slope = 1
            elif ratings[i] < ratings[i-1]:
                cur_slope = -1
            else:
                cur_slope = 0
            if ((pre_slope > 0) and (0 == cur_slope)) or ((pre_slope < 0) and (cur_slope >= 0)):
                candies += ((ups * ups + ups) / 2) + ((downs * downs + downs) / 2) + max(ups, downs)
                ups = downs = 0
            if cur_slope > 0:
                ups += 1
            elif cur_slope < 0:
                downs += 1
            else:
                candies += 1
            pre_slope = cur_slope
        candies += ((ups * ups + ups) / 2) + ((downs * downs + downs) / 2) + max(ups, downs) + 1
        return candies

# debus
s = Solution()
print s.candy([1,0,2])
print s.candy([1,2,2])
print s.candy([1,3,2,2,1])
