class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        """
        a = int(a, 2)
        b = int(b, 2)
        c = a + b
        return "{:b}".format(c)
