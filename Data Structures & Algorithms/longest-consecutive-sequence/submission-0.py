class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hashset = set(nums)
        inits = [num for num in nums if num - 1 not in nums_hashset] 
        max_seq = 0
        for init in inits:
            end = init
            while end + 1 in nums_hashset:
                end += 1
            max_seq = max(end - init + 1, max_seq)
        return max_seq