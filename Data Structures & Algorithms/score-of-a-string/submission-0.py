class Solution:
    def scoreOfString(self, s: str) -> int:
        
        
        # EASY QUESTION 
        # T.C = O(n) CANNOT BE REDUCE MORE THAN THAT
        # S.C = O(1)
        total_score = 0
        
        for i in range(len(s) - 1):
            
            total_score += abs(ord(s[i]) - ord(s[i + 1]))
            
        return total_score
