class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for (idx, num) in enumerate(numbers):
            if target - num in numbers:
                return [idx + 1, numbers.index(target - num) + 1]