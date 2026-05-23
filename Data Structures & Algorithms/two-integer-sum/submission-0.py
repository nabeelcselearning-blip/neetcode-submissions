class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, elem in enumerate(nums):
            diff = target - elem

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[elem] = i
