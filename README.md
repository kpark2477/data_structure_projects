# data_structure_projects
Udacity 자료구조&알고리즘 코스의 자료구조 프로젝트입니다.
총 6가지 문제로 구성이 되어있고, 주어진 문제에 맞추어 자료구조를 만드는 문제입니다.
(arrays, stacks, queue, recursion, tree, hashmap 등의 개념을 다룹니다.)


개별문제 해답에 대한 디자인과 time complexity는 
[`./explanation.md`](./explanation.md) 에서 확인하실 수 있습니다.

문제 내용은 아래와 같습니다.

## 1.Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.
The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
While doing the get() operation, if the entry is found in the cache, it is known as a cache hit.
If, however, the entry is not found, it is known as a cache miss.
When designing a cache, we also place an upper bound on the size of the cache.
If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element.
After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.
For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache.
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
For the current problem, consider both get and set operations as an use operation.
Your job is to use an appropriate data structure(s) to implement the cache.
In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. 
If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.
For the current problem, you can consider the size of cache = 5.

## 2.File recursion
For this problem, the goal is to write code for finding all files under a directory
(and all directories beneath it) that end with ".c"

## 3.Huffman coding
implement huffman coding and decoding.

## 4.Active directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such.
Where User is represented by str representing their ids.
Write a function that provides an efficient look up of whether the user is in a group.

## 5.Blockchain
A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
Use your knowledge of linked lists and hashing to create a blockchain implementation.

## 6.Union and Intersection of two linked list.
Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.
You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.
