class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()

        # Create the hash table where each element in nums points to its indices
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]] = []
            hash_table[nums[i]].append(i)

        # Now check for each num if the target-diff is also in hash_table
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_table:
                # If diff and num are not the same and we found indices
                if diff != num:
                    return [i, hash_table[diff][0]]
                else:
                    # If they are the same, we need at least 2 occurrences
                    if len(hash_table[diff]) >= 2:
                        return [i, hash_table[diff][1]]  # Second occurrence index
        return []

        

        