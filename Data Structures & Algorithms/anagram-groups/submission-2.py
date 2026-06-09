class Solution:
    def groupAnagrams(self, strs: List[str]):
        res = defaultdict(list) # mapping char counts (key) to list of anagrams (value)

        for s in strs:
            countKey = [0] * 26 # a ... z

            for c in s:
                countKey[ord(c) - ord("a")] += 1 #ASCII char 
            
            res[tuple(countKey)].append(s) #we are appending s (value) to the key (countKey) and it is tuple cause keys cannot be mutuable

        return list(res.values())
