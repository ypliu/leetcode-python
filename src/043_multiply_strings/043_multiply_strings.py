class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if "0" == num1 or "0" == num2:
            return "0"
        if "" == num1 or "" == num2 or None == num1 or None == num2:
            return ""

        dict_ch2n = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        str_n2ch = "0123456789"
        product_digits = len(num1) + len(num2)
        product_array = [0 for i in xrange(product_digits)]
        # simulate the process of bitwise multiplication
        for i in xrange(len(num1)):
            factor1 = dict_ch2n[num1[i]]
            for j in xrange(len(num2)):
                product_array[i+j+1] += factor1 * dict_ch2n[num2[j]]
        # carry to higher-order digit and store remainder if it is greater than 10 from the lowest
        for i in xrange(product_digits-1, 0, -1):
            product_array[i-1] += product_array[i] / 10
            product_array[i] = product_array[i] % 10

        res = ""
        i = 1 if 0 == product_array[0] else 0
        while i < product_digits:
            res += str_n2ch[product_array[i]]
            i += 1
        return res

# debug
s = Solution()
print s.multiply("2", "3")
print s.multiply("123", "456")
