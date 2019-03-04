class Solution:
    def nextGreaterElements(self, nums: 'List[int]') -> 'List[int]':
        result = [None for _ in range(len(nums))]
        stack = []
        M = len(nums)

        for i in range(2*len(nums)-1, -1, -1):
            i = i % M
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            result[i] = nums[stack[-1]] if stack else -1
            stack.append(i)
        return result
