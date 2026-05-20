class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # advance the left until target - numbers[left] is greater than numbers[right], and then switch
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                # increase the target
                left += 1
            else:
                right -= 1
        print(False, "something went wrong; twoSum not found")