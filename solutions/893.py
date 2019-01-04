class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = set()
        for element in A:
            odd = []
            even = []
            for i, c in enumerate(element):
                if i % 2 == 0:
                    odd.append(c)
                else:
                    even.append(c)
            odd.sort()
            even.sort()
            odd = ''.join(odd)
            even = ''.join(even)
            result.add((odd, even))
        return len(result)