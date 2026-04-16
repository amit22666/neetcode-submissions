# insertion at the end -> O(1)
# deletion from first -> O(1)
# bring a node at end -> O(1)

# if we choose dll then to insert and delete we need that node*
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key to Node object
        
        # Dummy nodes to avoid null checks
        self.left = Node(0, 0)  # Least Recently Used (LRU) side
        self.right = Node(0, 0) # Most Recently Used (MRU) side
        self.left.next = self.right
        self.right.prev = self.left
         
    def remove(self, node):
        """Removes a node from the linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """Inserts a node at the end (right side), just before the dummy right node."""
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move to the end (Most Recently Used)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node position
            self.remove(self.cache[key])
        
        # Create/Update node and insert at the MRU end
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # 1. Identify the LRU node (the one after the left dummy)
            lru_node = self.left.next
            # 2. Remove it from the linked list
            self.remove(lru_node)
            # 3. Remove it from the hash map using its key
            del self.cache[lru_node.key]
