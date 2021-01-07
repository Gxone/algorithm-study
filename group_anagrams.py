class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rst = collections.defaultdict(list)
        
        for s in strs:
            rst[''.join(sorted(s))].append(s)

        return rst.values()
