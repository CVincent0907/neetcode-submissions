class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = dict()

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1 

        lst = []
        if k > len(hash_table):
            return lst 

        for i in range(k):
            maxKey = max(hash_table, key = hash_table.get) # return key with largest value from hash_table
            lst.append(maxKey)
            del hash_table[maxKey]
        
        return lst 
        