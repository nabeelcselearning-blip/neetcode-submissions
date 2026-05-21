class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = []
        for i in range(0,len(nums)):
            if nums[i] in arr:
                return True
            arr.append(nums[i])
        
        return False
            

        
        
        
        
        
        
        
        
        
        
        # FIRST TRY
        
        # for elem_1 in nums:
        #     count = 0
        #     for elem_2 in nums:
        #         if elem_1 == elem_2:
        #             count += 1
        #         if count > 1:
        #             return True
        
        # return False

        # TIME COMPLEXITY = O(n^2)
        # SPACE COMPLEXITY = O(1)
        # WITH USE OF INDEXING WE CAN REMOVE COUNT COND.
        # ON SUBMISSION TIME LIMIT EXCEEDS
        