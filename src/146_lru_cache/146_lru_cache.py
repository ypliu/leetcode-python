class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.queue = [None] * capacity
        self.dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.queue.remove(key)
            self.queue.append(key)
            self.dict[key] = value
            return
        else:
            if None not in self.queue:
                del self.dict[self.queue[0]]
            self.queue.pop(0)
            self.queue.append(key)
            self.dict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# debug
cache = LRUCache(2)
cache.put(1, 1);
cache.put(2, 2);
print cache.get(1); # returns 1
cache.put(3, 3);    # evicts key 2
print cache.get(2); # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
print cache.get(1); # returns -1 (not found)
print cache.get(3); # returns 3
print cache.get(4); # returns 4
