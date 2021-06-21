# LeetCode Practice - 146. LRU Cahce


### Tag：`Design`
### Difficulty: Medium
### Link：https://leetcode.com/problems/lru-cache/

<br>

## Description:

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- `LRUCache(int capacity)` Initialize the LRU cache with positive size capacity.

- `int get(int key)` Return the value of the key if the key exists, otherwise return -1.

- `void put(int key, int value)` Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

<br>

## Scratches
LRU structure: hash + double linked list
<img src="https://github.com/Zhaoyh-Jonathan/LeetCodePractice/blob/main/imgs/LRU_scratch.png?raw=true" alt="LRU basic structure">

<br>

## My Solution:
```java
class LRUCache {
    class Node {
        public int key, val;
        public Node prev, next;
        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
    
    class DoubleLinkedList {
        public Node head, tail;
        public int size;
        public DoubleLinkedList() {
            head = tail = null;
            size = 0;
        }
        
        public void addFirst(Node x) {
            if (size == 0) {
                head = tail = x;
            } else {
                x.next = head;
                head.prev = x;
                head = x;
            }
            size++;
        }
        
        // return the key to also remove the key-val pair in hash later
        public int removeLast() {
            int key = -1;
            if (size == 0) {
                return key;  // cannot remove the last element
            } else if (size == 1) {
                key = tail.key;
                head = tail = null;
            } else {
                key = tail.key;
                tail = tail.prev;
                tail.next = null;
            }
            size--;
            return key;
        }
            
        // node x must exist (check before calling
        public void remove(Node x) {
            if (size == 1) {
                head = tail = null;
            } else if (head == x) {
                head = x.next;
                head.prev = null;
            } else if (tail == x) {
                tail = x.prev;
                tail.next = null;
            } else {
                x.prev.next = x.next;
                x.next.prev = x.prev;
            }
            size--;
        } 
            
        public int getSize() {
            return size;
        }
    }
    
    
    private Map<Integer, Node> htable;
    private DoubleLinkedList doubleList;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        htable = new HashMap<Integer, Node>();
        doubleList = new DoubleLinkedList();
    }
    
    public int get(int key) {
        if (!htable.containsKey(key)) {  // not found
            return -1;
        } 
        if (doubleList.getSize() == 1) {
            return doubleList.head.val;
        }

        int val = htable.get(key).val;
        put(key, val);
        return val;
    }
    
    public void put(int key, int value) {
        Node node = new Node(key, value);
        
        if (htable.containsKey(key)) {  // exists, update val        
            doubleList.remove(htable.get(key));
            doubleList.addFirst(node);
        } else {
            if (doubleList.getSize() + 1 > capacity) {
                htable.remove(doubleList.removeLast());
            }
            doubleList.addFirst(node);
        }
        htable.put(key, node);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

### Notes:
Reference to Java LinkedHashMap.