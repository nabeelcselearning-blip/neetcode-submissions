class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Dictionary search → O(1) average
        d = {} 
        for elem in nums:
            if elem in d:
                return True
            d[elem] = 1
        return False




        # SOLN SUBMITTED BUT STILL TIME COMPL is approx O(n^2)
        # AS I AM STILL USING TWO LOOPS, (if nums[i] in arr) it costs linear search T.C
        # arr = []
        # for i in range(0,len(nums)):
        #     if nums[i] in arr:
        #         return True
        #     arr.append(nums[i])
        
        # return False
            

        
        
        
        
        
        
        
        
        
        
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
        