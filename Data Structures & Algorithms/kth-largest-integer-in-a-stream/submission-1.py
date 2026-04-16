# Import the heapq module from the standard library (for min-heap)

# Define the KthLargest class
class KthLargest:

    # Constructor: initialize with k and nums
    def __init__(self, k: int, nums: List[int]):
        # Store k
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

        # Initialize a min-heap using nums
        # Use heapq.heapify to convert nums into a heap
        # While the heap size is larger than k, remove the smallest element

    # Add method: insert a new value into the stream
    def add(self, val: int) -> int:
        # Push the new value into the heap
        # If the heap size exceeds k, pop the smallest element
        # Return the smallest element in the heap (this is the kth largest)
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]