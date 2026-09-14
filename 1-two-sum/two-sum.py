class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in prevNums:
                return (i,prevNums[diff])
            prevNums[num] = i
        