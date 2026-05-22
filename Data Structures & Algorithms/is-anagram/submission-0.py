class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_t = {}
        dict_s = {}

        for i in range(len(s)):
            if t[i] in dict_t:
                c = dict_t.get(t[i])
                dict_t[t[i]] = c+1

            else:
                dict_t[t[i]] = 1
            
            if s[i] in dict_s:
                c = dict_s.get(s[i])
                dict_s[s[i]] = c+1
            
            else:
                dict_s[s[i]] = 1
        
        if dict_t == dict_s:
            return True
        
        return False
            