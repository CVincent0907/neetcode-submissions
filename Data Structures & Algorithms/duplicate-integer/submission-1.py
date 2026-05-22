class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = dict()
        for i in range(len(nums)):
            if (nums[i] in hash_table.keys()):
                return True 
            hash_table[nums[i]] = "Inserted"
        return False 
        
         