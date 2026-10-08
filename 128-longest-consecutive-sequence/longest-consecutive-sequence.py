class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #Transform the array into a set
        numSet = set(nums)
        longest = 0
        '''check if for each number in the set there is the one before, when we reach the base of the sequence, we check if there is the next one in a while loop until we calculated the lenght of the sequence, and save the max between the longest we had already found and the one we just found, then simply return the longest'''
        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                longest = max(longest,length)
        return longest