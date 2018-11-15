# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """

        def gcdCompute(num1, num2):
            if num1 < 0:
                num1 = -num1
            if num2 < 0:
                num2 = -num2
            if num1 < num2:
                num1, num2 = num2, num1
            while num2 != 0:
                r = num1 % num2
                num1 = num2
                num2 = r
            return num1

        if not points:
            return 0
        res = 0
        for i in range(len(points)):
            hash_t = {'v': 1}; duplicate = 0
            xi, yi = points[i].x, points[i].y
            for j in range(i+1, len(points)):
                delta_x, delta_y = points[j].x-xi, points[j].y-yi
                if 0 == delta_x:
                    if 0 == delta_y:
                        slope = 'd'
                        duplicate += 1
                    else:
                        slope = 'v'
                else:
                    # slope = (yj - yi) * 1.0 / (xj - xi)
                    gcd = gcdCompute(delta_x, delta_y)
                    delta_x //= gcd; delta_y //= gcd
                    if delta_x > 0:
                        slope = (delta_x, delta_y)
                    else:
                        slope = (-delta_x, -delta_y)
                if slope == 'd':
                    continue
                elif slope not in hash_t:
                    hash_t[slope] = 2
                else:
                    hash_t[slope] += 1
            res = max(max(hash_t.values()) + duplicate, res)
        return res

# debug
s = Solution()
points = [ Point(1,1), Point(2,2), Point(3,3) ]
print s.maxPoints(points)
points = [ Point(1,1), Point(3,2), Point(5,3), Point(4,1), Point(2,3), Point(1,4) ]
print s.maxPoints(points)
points = [ Point(0,0), Point(0,0) ]
print s.maxPoints(points)
points = [ Point(0,0) ]
print s.maxPoints(points)
points = [ Point(0,0), Point(94911151,94911150), Point(94911152,94911151) ]
print s.maxPoints(points)
print s.maxPoints(None)
print s.maxPoints([])
