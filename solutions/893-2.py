class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = set()
        for element in A:
            even = sorted(element[0::2])
            odd = sorted(element[1::2])
            even = ''.join(even)
            odd = ''.join(odd)
            result.add((even, odd))
        return len(result)