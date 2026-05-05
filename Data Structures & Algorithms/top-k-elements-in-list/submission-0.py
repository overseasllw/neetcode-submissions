class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequences = Counter(nums)

        heap = []
        for num,freq in frequences.items():
            if len(heap) < k:
                heapq.heappush(heap,(freq,num))
            else:
                if freq > heap[0][0]:
                    heapq.heappushpop(heap,(freq,num))

        return [num for _,num in heap]