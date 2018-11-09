# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return None
        hash_table = {}
        hash_table[None] = None; hash_table[head] = dummy = RandomListNode(head.label)
        temp = head
        while temp:
            temp_copy = hash_table[temp]
            if temp.random:
                if not (temp.random in hash_table):
                    hash_table[temp.random] = RandomListNode(temp.random.label)
                temp_copy.random = hash_table[temp.random]
            if not (temp.next in hash_table):
                hash_table[temp.next] = RandomListNode(temp.next.label)
            temp_copy.next = hash_table[temp.next]
            temp = temp.next
        return dummy

# debug
head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
s = Solution()
s.copyRandomList(head)
