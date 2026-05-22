class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in hash_table:
                hash_table[num] = i
            else:
                return [hash_table[diff], i]
        return []


        

        