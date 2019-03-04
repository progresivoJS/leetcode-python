class Solution:
    def nextGreaterElements(self, nums: 'List[int]') -> 'List[int]':
        result = []
        M = len(nums)
        for i, num in enumerate(nums):
            j = i+1
            while j % M != i:
                if num < nums[j % M]:
                    result.append(nums[j % M])
                    break
                j += 1
            else:
                result.append(-1)
        return result
