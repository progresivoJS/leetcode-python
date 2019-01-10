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
                    .replace('!', ' ')   \
                    .replace('?', ' ')   \
                    .replace('.', ' ')   \
                    .replace(',', ' ')   \
                    .replace(';', ' ')   \
                    .replace('\'', ' ')  \
                    .lower()
        
        dic = collections.Counter(paragraph.split())
        
        most_frequent_word, count = '', 0
        for key, value in dic.items():
            if count < value and key not in banned:
                most_frequent_word = key
                count = value
        return most_frequent_word