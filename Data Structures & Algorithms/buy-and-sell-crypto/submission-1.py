class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        biggest_difference = 0
        for price in prices[1:]:
            if price < lowest:
                lowest = price
            elif price - lowest > biggest_difference:
                biggest_difference = price - lowest
        return biggest_difference