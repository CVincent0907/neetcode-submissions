class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = dict() 
        for e in strs:
            sorted_e = Solution.sort(e)
            if sorted_e not in hash_table: 
                hash_table[sorted_e] = [e]
            else:
                hash_table[sorted_e] = hash_table.get(sorted_e) + [e]
        
        return list(hash_table.values())

    @staticmethod 
    def sort(string):
        return ''.join(sorted(string))

