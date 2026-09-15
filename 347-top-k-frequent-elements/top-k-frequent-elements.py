class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFrequency = defaultdict(int)
        for number in nums:
            numsFrequency[number] = numsFrequency[number] + 1
        sortedFrequency = sorted(numsFrequency, key=numsFrequency.get, reverse=True)
        return sortedFrequency[:k]