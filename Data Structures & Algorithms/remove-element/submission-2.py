class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        
        occurences_val = nums.count(val)
        safe_range = len(nums)-occurences_val
        
        c = 0
        while c < safe_range:
            for i in range(len(nums)):
                if nums[c] == val:
                    del nums[c]
                    c -= 1
                c+= 1
            return safe_range
        
        return safe_range
