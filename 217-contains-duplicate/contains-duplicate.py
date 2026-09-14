class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevNums = set()
        for num in nums:
            if num in prevNums:
                return True
            prevNums.add(num)
        return False