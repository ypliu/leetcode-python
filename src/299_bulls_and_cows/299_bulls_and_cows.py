class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        count_A = count_B = 0
        counts = [0 for _ in range(10)]
        for i in range(len(secret)):
            ch_s,ch_g = secret[i],guess[i]
            if (ch_s == ch_g):
                count_A += 1
            else:
                d_s,d_g = (ord(ch_s)-ord('0')),(ord(ch_g)-ord('0'))
                if (counts[d_s] < 0):
                    count_B += 1
                if (counts[d_g] > 0):
                    count_B += 1
                counts[d_s] += 1
                counts[d_g] -= 1
        # return str(count_A) + 'A' + str(count_B) + 'B'
        return "{}A{}B".format(str(count_A), str(count_B))

# debug
s = Solution()
print s.getHint("1807", "7810")
print s.getHint("1123", "0111")
