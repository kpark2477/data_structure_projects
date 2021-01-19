from collections import OrderedDict

class LRU_Cache:
    def __init__(self, capacity = 5):
        assert capacity >= 1, "Capacity should be at least 1."
        self.dict = OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if self.dict.get(key):
            self.dict.move_to_end(key)
            return self.dict.get(key)
        else:
            return -1

    def set(self, key, value):
        if self.dict.get(key):
            self.dict[key] = value
            self.dict.move_to_end(key)
        else:
            if self.size < self.capacity:
                self.dict[key] = value
                self.size += 1
            else:
                self.dict.popitem(last=False)
                self.dict[key] = value


test1_cache = LRU_Cache(5)

test1_cache.set(1, 1)
test1_cache.set(2, 2)
test1_cache.set(3, 3)
test1_cache.set(4, 4)

print(test1_cache.get(1))       # returns 1
print(test1_cache.get(2))       # returns 2
print(test1_cache.get(9))      # returns -1 because 9 is not present in the cache
test1_cache.set(5, 5)
test1_cache.set(6, 6)
print(test1_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


test2_cache = LRU_Cache(1)
test2_cache.set(1, 1)
test2_cache.set(2, 2)

print(test2_cache.get(1)) # returns -1 because the cache reached it's capacity and 1 was the least recently used entry
print(test2_cache.get(2)) # returns 2


test3_cache = LRU_Cache(5)
test3_cache.set(1, 1)
print(test3_cache.get(2))  # returns -1
test3_cache.set(1, 11111)
print(test3_cache.get(1))  # overriding a value, returns 11111

test3_cache = LRU_Cache(0) # gives an error, because cache should has at least capacity of 1.
        
