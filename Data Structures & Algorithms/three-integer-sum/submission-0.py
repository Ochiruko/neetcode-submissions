# requires numbers to be sorted. Also no repeats; not sure if it will work with repeats.
def twoSum(nums: List[int], target: int) -> List[int]:
    sums = []
    i = 0
    j = len(nums) - 1
    while j >= i:
        if nums[i] + nums[j] == target:
            sums.append([nums[i], nums[j]])
            j -= 1
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1        
        elif nums[i] + nums[j] < target:
            i += 1
    return sums

class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution
        num_to_ixs = dict()
        for ix, num in enumerate(nums):
            num_to_ixs.setdefault(num, set()).add(ix)
        sums = []
        sorted_nums = sorted(num_to_ixs.keys())
        for l in sorted_nums:
            two_sums = twoSum(sorted_nums, -l)
            if two_sums == []: continue
            for m, r in two_sums:
                sums.append([l, m, r])
        indices = set()
        for l, m, r in sums:
            l_ixs = num_to_ixs[l]
            m_ixs = num_to_ixs[m]
            r_ixs = num_to_ixs[r]
            indices.update({tuple(sorted([l_ix, m_ix, r_ix]))
                            for l_ix in l_ixs 
                            for m_ix in m_ixs
                            for r_ix in r_ixs
                            if l_ix != m_ix and m_ix != r_ix and l_ix != r_ix})
        return [[l, m, r] for l, m, r in ({tuple(sorted([nums[l],nums[m],nums[r]])) for l,m,r in indices})]