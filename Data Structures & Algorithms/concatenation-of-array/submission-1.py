class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums+nums
        return ans

        # return nums * 2 [1,2,3] * [1,2,3] = [1,2,3,1,2,3]