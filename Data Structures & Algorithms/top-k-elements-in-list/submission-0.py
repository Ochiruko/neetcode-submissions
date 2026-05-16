class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # presumably uses a heap
        return [xs[0] for xs in Counter(nums).most_common(k)]
        # get_frequency = lambda num: frequency[num]
        # return heapq.nlargest(nums, key=get_frequency)