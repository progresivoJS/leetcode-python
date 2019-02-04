class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        box = set()
        for num in nums:
            if num in box:
                box.remove(num)
            else:
                box.add(num)
        return box.pop()
