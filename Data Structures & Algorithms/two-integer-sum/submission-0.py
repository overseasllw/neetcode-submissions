class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}
        for i,num in enumerate(nums):
            difference  =  target - num
            if difference in compliment:
                j = compliment[difference]

                return [min(i,j),max(i,j)]
            compliment[num] = i
        return []
    
