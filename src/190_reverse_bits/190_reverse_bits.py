class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # return int(bin(n)[2:].zfill(32)[::-1], 2)
        return self.reverseBitsNaive(n)
        return self.reverseBitsAwesome(n)

    def reverseBitsNaive(self, n):
        if 0 == n:
            return 0
        res = 0
        for i in range(32):
            res <<= 1
            res |= (n & 1)
            n >>= 1
        return res

    def reverseBitsAwesome(self, n):
        # https://leetcode.com/problems/reverse-bits/discuss/54741/O(1)-bit-operation-C%2B%2B-solution-(8ms)
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n

# debug
s = Solution()
print s.reverseBits(43261596)
