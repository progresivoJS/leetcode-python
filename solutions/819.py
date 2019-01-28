class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph
        = paragraph.replace('!', ' ')   \
                    .replace('?', ' ')   \
                    .replace('.', ' ')   \
                    .replace(',', ' ')   \
                    .replace(';', ' ')   \
                    .replace('\'', ' ')  \
                    .lower()
        dic = {}
        for word in paragraph.split():
            try:
                dic[word] += 1
            except KeyError:
                dic[word] = 1
        for item in sorted(dic.items(), key=lambda kv: kv[1], reverse=True):
            if item[0] not in banned:
                return item[0]
