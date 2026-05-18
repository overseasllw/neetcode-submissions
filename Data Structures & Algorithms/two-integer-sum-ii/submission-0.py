class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        reminder = {}

        for ind,val in enumerate(numbers):
            if reminder.get(target - val):
                return [reminder.get(target - val),ind+1]
            reminder[val] = ind + 1
        return []
                
