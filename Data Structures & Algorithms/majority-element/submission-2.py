class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # OPTIMAL SOLN
        # T.C = O(n)
        # S.C = O(1)
        # ALGO NAME = Boyer-Moore Voting Algorithm
        element = nums[0]
        count = 0

        for i in range(len(nums)):
            if element == nums[i]:
                count += 1
            else:
                count -= 1

            if count == 0:
                element = nums[i]
                count += 1 #in last submission i forgot to add count as elemt changes count increases
            
            if count > len(nums)//2:
                return element

        return element 


        # in interviews do not use in-built fn write ur own sorting algo
        # BETTER SOLN BUT NOT OPTIMAL
        # nums.sort() #sorting the list in-place
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     count += 1
        #     if count > n//2:
        #         return nums[i]
        #     if count < n//2 and i < len(nums) -1 and nums[i] != nums[i+1]:
        #         count = 0
        
        # return 

        # T.C = O(nlogn) + O(n)
        # S.C = O(1)