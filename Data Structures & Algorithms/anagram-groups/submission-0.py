class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list) # an empty list for each new key
        for s in strs:
            sortedS = ''.join(sorted(s))
            hashMap[sortedS].append(s)
        return list(hashMap.values())