class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
       

        for i in nums:
            result += [subset + [i] for subset in result]
        return result