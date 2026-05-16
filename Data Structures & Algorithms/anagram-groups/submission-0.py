class Solution:    
    # I use a clever workaround to having frozendicts: sorting.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, list[str]] = dict()
        for s in strs:
            s_chars = str(sorted(s))
            if s_chars not in anagrams:
                anagrams[s_chars] = []
            anagrams[s_chars].append(s)
        return list(anagrams.values())
