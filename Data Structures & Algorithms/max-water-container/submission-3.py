def area(l, r, heights):
    return (r - l) * min(heights[l], heights[r])


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best_area = area(l, r, heights)
        while l < r:
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            best_area = max(area(l, r, heights), best_area)
        return best_area