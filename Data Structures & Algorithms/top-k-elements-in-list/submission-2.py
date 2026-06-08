class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countN = {}
        for n in nums:
            countN[n] = 1 + countN.get(n, 0)

        lis = []
        for n, count in countN.items():
            lis.append([count, n])
        lis.sort()

        res = []
        while len(res)<k:
            res.append(lis.pop()[1])

        return res
        