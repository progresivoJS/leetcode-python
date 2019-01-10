class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        dic = {}
        paragraph = paragraph           \
                    .replace('!', ' ')  \
                    .replace('?', ' ')  \
                    .replace('.', ' ')  \
                    .replace(',', ' ')  \
                    .replace(';', ' ')  \
                    .replace('\'', ' ') \
                    .lower()            \
                    .split()
        
        paragraph = [word for word in paragraph if word not in banned]
        dic = collections.Counter(paragraph)
        return max(dic.keys(), key = lambda kv: dic[kv])
        