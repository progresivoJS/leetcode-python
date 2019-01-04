class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            local_name, domain = email.split('@')
            local_name = local_name.replace('.', '')
            local_name = local_name[0:local_name.find('+')]
            result.add('@'.join((local_name, domain)))
        return len(result)