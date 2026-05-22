from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates easily
        result = []

        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            temp = 0 - nums[i]
            j = len(nums) - 1
            k = i + 1

            while k < j:
                two_sum = nums[k] + nums[j]

                if two_sum < temp:
                    k += 1
                elif two_sum > temp:
                    j -= 1
                else:
                    result.append([nums[i], nums[k], nums[j]])

                    k += 1
                    j -= 1

                    # Skip duplicates for the second and third numbers
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1
                    while k < j and nums[j] == nums[j + 1]:
                        j -= 1

        return result






