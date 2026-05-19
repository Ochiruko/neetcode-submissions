class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = []
        right_prods = []

        left_prod = 1
        for num in nums:
            left_prods.append(left_prod)
            left_prod *= num

        right_prod = 1
        for num in reversed(nums):
            right_prods.append(right_prod)
            right_prod *= num
        right_prods.reverse()

        return [l * r for (l, r) in zip(left_prods, right_prods)]