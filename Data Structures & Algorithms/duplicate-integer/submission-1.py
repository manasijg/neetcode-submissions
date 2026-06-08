class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = []

        for i in range(len(nums)):
            if nums[i] not in dupe:
                dupe.append(nums[i])
            
        return dupe != nums
