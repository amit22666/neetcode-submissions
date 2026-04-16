// A struct to hold element and its frequency
type Element struct {
	num  int
	freq int
}

// PriorityQueue implements heap.Interface and holds Elements
type PriorityQueue []Element

func (pq PriorityQueue) Len() int            { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool  { return pq[i].freq < pq[j].freq } // Min-Heap by frequency
func (pq PriorityQueue) Swap(i, j int)       { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(Element)) }
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[:n-1]
	return item
}

// topKFrequent returns k most frequent elements
func topKFrequent(nums []int, k int) []int {
	// Step 1: Count frequencies
	freqMap := make(map[int]int)
	for _, num := range nums {
		freqMap[num]++
	}

	// Step 2: Use Min-Heap of size k
	pq := &PriorityQueue{}
	heap.Init(pq)

	for num, freq := range freqMap {
		heap.Push(pq, Element{num, freq})
		if pq.Len() > k {
			heap.Pop(pq) // remove smallest freq element
		}
	}

	// Step 3: Extract elements from heap
	result := make([]int, 0, k)
	for pq.Len() > 0 {
		result = append(result, heap.Pop(pq).(Element).num)
	}

	return result
}