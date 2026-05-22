class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # BETTER IDEA
        # Instead of building two dictionaries separately:
        # 👉 build only ONE frequency map

        # Add for s
        # Subtract for t

        # Then check if everything becomes zero meaning if all keys of dict are zero or not
        # if zero means angram else not an angram

        if len(s) != len(t):
            return False


        dict_record = {}
        for i in range (len(s)):
            
            # REMEBER THIS WAY OF DOING
            dict_record[s[i]] = dict_record.get(s[i], 0) + 1 
            dict_record[t[i]] = dict_record.get(t[i], 0) - 1

        return all(value == 0 for value in dict_record.values())


        # PROBLEM WITH THIS APPROACH
        # You are building:

        # dict_s
        # dict_t
        # That means:

        # Two full passes of counting
        # Two data structures
        # Final full dictionary comparison

        # So even though it’s:

        # Time: O(n)
        # Space: O(k)
        # 👉 It’s doing redundant work



        # if len(s) != len(t):
        #     return False
        
        # dict_t = {}
        # dict_s = {}

        # for i in range(len(s)):
        #     if t[i] in dict_t:
        #         c = dict_t.get(t[i])
        #         dict_t[t[i]] = c+1

        #     else:
        #         dict_t[t[i]] = 1
            
        #     if s[i] in dict_s:
        #         c = dict_s.get(s[i])
        #         dict_s[s[i]] = c+1
            
        #     else:
        #         dict_s[s[i]] = 1
        
        # if dict_t == dict_s:
        #     return True
        
        # return False
            