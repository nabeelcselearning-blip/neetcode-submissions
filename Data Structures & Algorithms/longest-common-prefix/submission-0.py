class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        # Horizontal Character Comparison
        # It compares characters column by column.    
        # Complexity
        #   T(n,m)=O(n×m)
        # Space:
        #   S(m)=O(m)
        lcp = ""
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return lcp 
            lcp += strs[0][i]
        
        # when all words are same in a string loop will finish successfully 
        return lcp 