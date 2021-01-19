from datetime import datetime

import hashlib


class Block():

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return "time %s, data %s, prev_hash %s, hash %s" % (self.timestamp, self.data, self.previous_hash, self.hash)


class BlockChain():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.size == 0:
            new_block = Block(data, 0)
            self.head = new_block
            self.tail = new_block
            self.size += 1
            return f"{new_block.data} is added to the chain"
        else:
            new_block= Block(data, self.tail.hash)
            self.tail.next = new_block
            self.tail = self.tail.next
            self.size += 1
            return f"{new_block.data} is added to the chain"

    def __repr__(self):
        output = "\nLet's view the chain:\nThe number of elements are %s" % (self.size)

        if self.size == 0:
            output += "\n There's no block in the chain"
            return output

        current_block = self.head
        output += '\n[{}] '.format(current_block.data)

        while current_block.next:
            current_block = current_block.next
            output += '\n[{}] '.format(current_block.data)
        
        return output

### Test case 1
test_1 = BlockChain()
test_1.add("hey")
test_1.add("yo")
previous_hash = test_1.tail.hash # save tail's hash.
test_1.add("ohyeah")

print(test_1) # This should return all the block data that were added.
print(test_1.tail.previous_hash == previous_hash) # This should return True, because added block should contain previous hash.

### Test case 2
test_2 = BlockChain()
test_2.add("") # Edge case, empty string.
test_2.add("yo")

print(test_2) # This should return all the block data that were added.
print(test_2.tail) #This should show last added block's information such as time, data, previous hash, and hash.

### Test case 3

test_3 = BlockChain()
test_3.add("korea")
test_3.add("usa")
previous_hash = test_3.tail.hash # save tail's hash.
test_3.add("canada")

print(test_3) # This should return all the block data that were added.
print(test_3.tail.previous_hash == previous_hash) # This should return True, because added block should contain previous hash.

