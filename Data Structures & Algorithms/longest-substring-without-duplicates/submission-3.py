class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_instances = dict()
        longest = 0 
        start = 0
        for i, c in enumerate(s):
            # if c was seen in this substring, log the length and make
            # the new substring the one that started after the original sighting.
            if c in last_instances and last_instances[c] >= start:
                if i - start > longest:
                    longest = i - start
                start = last_instances[c] + 1
            last_instances[c] = i
        return max(len(s) - start, longest)
