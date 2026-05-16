class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_i = dict()
        for i, num in enumerate(nums):
            if num not in num_to_i:
                num_to_i[num] = []
            num_to_i[num].append(i) 
        for i, num in enumerate(nums):
            if target - num in num_to_i:
                # the smaller index will ding first
                js = [j for j in num_to_i[target - num] if j != i]
                if js == []:
                    continue
                return [i, js[0]]