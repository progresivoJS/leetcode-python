class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start):
            """
            reverse nums from start to end
            """
            i = start
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = len(nums)-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        
        if i >= 0:
            j = len(nums)-1
            while True:
                if nums[j] > nums[i]:
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i+1)
        
