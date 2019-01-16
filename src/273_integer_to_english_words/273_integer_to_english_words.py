class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if (num < 0):
            return None
        elif (0 == num):
            return "Zero"
        triple_units = [ "", " Thousand", " Million", " Billion", " Trillion" ]
        num_gt_20 = [ "", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen" ]
        tens = [ "", "", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety" ]
        res = ""
        n_triples = -1
        while (num > 0):
            triple = num % 1000
            num //= 1000
            n_triples += 1
            if (0 == triple):
                continue
            reading = ""
            if (triple >= 100):
                reading += num_gt_20[triple // 100] + " Hundred"
            triple %= 100
            if (triple < 20):
                reading += num_gt_20[triple]
            else:
                reading += tens[triple // 10] + num_gt_20[triple % 10]
            res = reading + triple_units[n_triples] + res
        return res[1:]

# debug
s = Solution()
print s.numberToWords(123)
print s.numberToWords(12345)
print s.numberToWords(1234567)
print s.numberToWords(1234567891)
