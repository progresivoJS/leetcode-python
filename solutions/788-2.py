class Solution:
    invalid_numbers = "347"
    valid_numbers = "2569"
    
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(N):
            if self.is_good_number(i+1):
                count += 1
        return count

    def is_good_number(self, N):
        N = str(N)
        for invalid in self.invalid_numbers:
            if invalid in N:
                return False
        for valid in self.valid_numbers:
            if valid in N:
                return True
        return False