from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        def compare(x, y):
            return (1 if x + y < y + x else -1)


        nums = list(map(str, nums))
        
        nums.sort(key=cmp_to_key(compare))
        
        return "0" if nums[0] == "0" else "".join(nums)
