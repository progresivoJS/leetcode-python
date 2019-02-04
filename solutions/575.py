class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = len(candies) // 2
        box = set()
        for candy in candies:
            box.add(candy)
        return min(len(box), n)
