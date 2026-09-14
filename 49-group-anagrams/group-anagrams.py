class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            signature = str(sorted(string))
            anagrams[signature].append(string)
        return list(anagrams.values())

         