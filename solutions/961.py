class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        elements = set()
        for num in A:
            if num in elements:
                return num
            else:
                elements.add(num)
