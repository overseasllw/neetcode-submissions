class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        reminder = {}

        for ind,val in enumerate(numbers):
           l, r = ind +1, len(numbers) -1
           rem = target - val

           while l <= r:
            mid = l + (r-l) // 2
            if numbers[mid]  == rem:
                return [ind+1,mid+1]
            elif numbers[mid] < rem:
                l = mid + 1
            else:
                r = mid - 1
        return []
                
