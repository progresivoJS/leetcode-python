class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = {}
        for count, domain in (cpdomain.split() for cpdomain in cpdomains):
            for subdomain in self.make_subdomains(domain):
                try:
                    counter[subdomain] += int(count)
                except KeyError:
                    counter[subdomain] = int(count)

        result = []
        for key, value in counter.items():
            result.append(f'{value} {key}')
        return result

    def make_subdomains(self, domain):
        yield domain
        i = 0
        while i < len(domain):
            if domain[i] == '.':
                yield domain[i+1:]
            i += 1
