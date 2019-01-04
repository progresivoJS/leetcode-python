class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_dic = dict(zip(string.ascii_lowercase, morse))
        
        result = set()
        for word in words:
            morse_code = []
            for c in word:
                morse_code.append(morse_dic[c])
            morse_code = "".join(morse_code)
            result.add(morse_code)
        return len(result)