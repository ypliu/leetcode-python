class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        return self.compareVersionTranNum(version1, version2)
        return self.compareVersionBasedSplit(version1, version2)

    def compareVersionTranNum(self, version1, version2):
        num1 = num2 = 0
        i,j = 0,0
        while (i < len(version1)) or (j < len(version2)):
            while (i < len(version1)) and (version1[i] != '.'):
                num1 = num1 * 10 + ord(version1[i]) - ord('0')
                i += 1
            while (j < len(version2)) and (version2[j] != '.'):
                num2 = num2 * 10 + ord(version2[j]) - ord('0')
                j += 1
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            num1 = num2 = 0
            i += 1; j += 1
        return 0

    def compareVersionBasedSplit(self, version1, version2):
        nums_version1 = [int(s) for s in version1.split('.')]
        nums_version2 = [int(s) for s in version2.split('.')]
        max_len = max(len(nums_version1), len(nums_version2))
        nums_version1 += [0] * (max_len - len(nums_version1))
        nums_version2 += [0] * (max_len - len(nums_version2))
        for i in range(max_len):
            if nums_version1[i] < nums_version2[i]:
                return -1
            elif nums_version1[i] > nums_version2[i]:
                return 1
        return 0

# debug
s = Solution()
print s.compareVersion("0.1", "1.1")
print s.compareVersion("1.0.1", "1")
print s.compareVersion("7.5.2.4", "7.5.3")
print s.compareVersion("01", "1")
print s.compareVersion("1.0", "1")
