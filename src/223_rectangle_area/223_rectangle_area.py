class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        area = (C-A) * (D-B) + (G-E) * (H-F)
        l,b = max(A,E),max(B,F)
        r,t = max(min(C,G),l),max(min(D,H),b)
        return (area - (r-l)*(t-b))

# debug
s = Solution()
print s.computeArea(-3,0,3,4,0,-1,9,2)
