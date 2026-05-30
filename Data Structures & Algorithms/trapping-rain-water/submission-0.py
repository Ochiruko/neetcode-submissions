class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        key = lambda i: height[i]
        two_highest = sorted(heapq.nlargest(2, range(len(height)), key=key))
        (lower, higher) = sorted(two_highest, key=key)
        if list(two_highest) == [0, len(height) - 1]:
            return (len(height) - 2) * height[lower] - sum(height[1:-1])
        else:
            left = self.trap(height[: two_highest[0] + 1])
            middle = self.trap(height[two_highest[0] : two_highest[1] + 1])
            right = self.trap(height[two_highest[1] :])
            return left + middle + right
