class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1; j = n - 1; index = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
            index -= 1
        while j >= 0:
            nums1[index] = nums2[j]
            index -= 1
            j -= 1

# debug
s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s.merge(nums1, 3, nums2, 3)
print nums1
