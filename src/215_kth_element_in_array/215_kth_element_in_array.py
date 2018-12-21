class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if (k < 1) or (k > len(nums)):
            return None
        # return self.findKthLargestBasedRandomPartition(nums, k)
        return self.findKthLargestBasedMinHeap(nums, k)
        

    def findKthLargestBasedRandomPartition(self, nums, k):
        import random
        if (1 == k):
            return max(nums)
        elif (len(nums) == k):
            return min(nums)
        def partition(arr):
            ig,key = 0,arr[-1]
            for i in range(len(arr)-1):
                if (arr[i] > key):
                    arr[ig],arr[i] = arr[i],arr[ig]
                    ig += 1
            arr[ig],arr[-1] = key,arr[ig]
            return ig+1
        r = random.randint(0, len(nums)-1)
        nums[-1],nums[r] = nums[r],nums[-1]
        p = partition(nums)
        if (p == k):
            return nums[p-1]
        elif (p < k):
            return self.findKthLargestBasedRandomPartition(nums[p:], k-p)
        else:
            return self.findKthLargestBasedRandomPartition(nums[:p-1], k)

    def findKthLargestBasedMinHeap(self, nums, k):
        import heapq
        min_heap = [n for n in nums[:k]]
        heapq.heapify(min_heap)
        for n in nums[k:]:
            if (n > min_heap[0]):
                heapq.heapreplace(min_heap, n)
        return min_heap[0]

# debug
s = Solution()
print s.findKthLargest([3,2,1,5,6,4], 2)
print s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
