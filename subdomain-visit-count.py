class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_count = defaultdict(int)
        
        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            fragments = domain.split('.')
            
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                subdomain_count[subdomain] += count
                
        return [f"{cnt} {sub}" for sub, cnt in subdomain_count.items()]