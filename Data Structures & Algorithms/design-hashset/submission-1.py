class MyHashSet:

    def __init__(self):
        # Choose a prime number for number of buckets to reduce collisions
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)] #(logic to create bucket) map simulate
        # Bucket
        # array -> []
        # linked list -> ListNode(0)
        # bst -> BST()

    def _hash(self, key: int) -> int:
        # Simple hash function: modulo
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)
        # Only add if key not already in bucket
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.buckets[h]
