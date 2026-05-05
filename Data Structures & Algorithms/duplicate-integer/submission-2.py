class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in nums:
            if duplicate.get(i):
                return duplicate.get(i)
            duplicate[i] = True
        return False