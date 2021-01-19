### Task1
## Design:
- For this task, We should keep track of cache use history to determine which key was used the most least recently.
- Orderddict was used to pop out first-in key, and move a key to the last when it is used.

## Time Complexity:
- O(C)
- Ordered dict function is implemented. and all operations in an ordered Dict are executed in constant time.

## Space Complexity:
- O(n)
- Dictionary size is limited by its capacity, So the space it takes won't exceed the limit.


### Task2
## Design:
- To find all the files, it should check all the sub folders under the current folder.
- Iterating through subfolders and recursively applying function to them is used to achieve it.

## Time Complexity:
- O(n)
- It iterate through all the subfolders and files "once".

## Space Complexity:
- O(n)
- It adds found items "once"


### Task3
## Design:
- First, I constructed node object which is pair of frequency and character.
- From there, the function keeps merging two least fequent characters into one node until there's only one node left which is root of the tree
- And that tree becomes the encoding and decoding tool.

## Time Complexity:
- O(n^2 +nlog(n))
- To check frequency of each character, it should go through the input -> O(n)
- To find smallest two nodes, it should iterate through the list twice, and then we need to repeat the process n times-> O(2n^2)
- And then to produce encoded data, we should traverse the tree -< nlog(n)

## Space Complexity:
- O(n)
- It would need space for freqency dict(n) and huffman tree(n)


### Task4
## Design:
- To search all the users, it should check all the sub groups under the parent group.
- recursive method is effective in this case.

## Time Complexity:
- O(n)
- It iterate through all the users "once".

## Space Complexity:
- O(n)
- It would need space for size of users.


### Task5
## Design:
- It's necessary to build a datastructure which keep tracing tail of it so that when new block is added it can automatically bring in previous hash data.
- I made sure that blockchain class keep track of and be easy to access to the tail block.

## Time Complexity:
- O(C)
- It only keeps adding new block to the chain. Time complexity would be Constant.

## Space Complexity:
- O(n)
- It would need space for the whold blocks.


### Task6
## Design:
- For intersection, I chose one node from the first list and compare it to all nodes from the other list. And then do the same process for the other nodes in the first list. 
- For Union, if you just sum up two lists, their intersection will be added twice. So I added all the nodes that don't have intersection with the other list first and then add the intersection once.

## Time Complexity:
- O(n**2)
- It has to compare all the nodes to all the nodes.

## Space Complexity:
- O(n)
- It would need space for the result linkedlist.


