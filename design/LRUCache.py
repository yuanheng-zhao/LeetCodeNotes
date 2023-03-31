from typing import Optional

class Node:
    def __init__(self, key=-1, val=0) -> None:
        self.key = key
        self.val = val
        self.prev = self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = self.tail = None
    
    def get_size(self) -> int:
        return self.size

    def add_first(self, node: Optional[Node]) -> None:
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def remove_last(self) -> int:        
        if self.size == 0:
            # invalid operation
            return -1
        key = self.tail.key
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return key

    def remove(self, node: Optional[Node]) -> None:
        if self.size == 0:
            return
        if self.size == 1:
            # skip validating the node is in the doubly linked list here
            self.head = self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # then the list has at least 3 elements
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

        

class LRUCache:
    """
    LeetCode 146. LRU Cache

    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU   

    Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.
    """
    def __init__(self, capacity: int) -> None:
        self.htable = {}
        self.doubly_linked_list = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.htable:
            return -1
        node = self.htable[key]
        self.doubly_linked_list.remove(node)
        self.doubly_linked_list.add_first(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.htable:
            self.doubly_linked_list.remove(self.htable[key])
        elif self.doubly_linked_list.get_size() + 1 > self.capacity:
                lru_key = self.doubly_linked_list.remove_last()
                self.htable.pop(lru_key)
        self.doubly_linked_list.add_first(node)
        self.htabl[key] = node
