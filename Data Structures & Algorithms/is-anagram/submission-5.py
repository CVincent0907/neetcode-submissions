
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table1 = dict()
        hash_table2 = dict() 

        for i in range(len(s)):
            hash_table1[s[i]] = hash_table1.get(s[i], 0) + 1
        
        for i in range(len(t)):
            hash_table2[t[i]] = hash_table2.get(t[i], 0) + 1
        
        return hash_table2 == hash_table1 
        # if (len(hash_table1) != len(hash_table2)):
        #     return False
        
        # for key in hash_table1.keys():
        #     if hash_table1.get(key, 0) != hash_table2.get(key, 0):
        #         return False
        # return True
        