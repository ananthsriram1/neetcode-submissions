from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for s in strs:
            index = str(sorted(s))
            mapping[index].append(s)

        rv = []
        for key in mapping:
            rv.append(mapping[key])

        return rv