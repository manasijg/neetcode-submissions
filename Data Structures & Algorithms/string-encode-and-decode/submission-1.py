class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res # res = ["4#neet4#code"]

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 #len of first string
        while i < len(s):
            j = i
            while s[j] != '#': #j=1 we find #
                j += 1
            length = int(s[i:j]) #we are extracting string from 0 to 1 which is len of first string = 4
            res.append(s[j+1:j+1+length]) #now we are appending from 2 to 6 = # s[2:6] = "neet"
            i = j+1+length #now we are skipping the first word as we decoded it so i = 6
        return res
