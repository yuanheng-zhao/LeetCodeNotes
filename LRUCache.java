import java.util.HashMap;

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