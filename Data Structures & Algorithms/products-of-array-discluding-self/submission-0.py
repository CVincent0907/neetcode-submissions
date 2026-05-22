class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []
        result = 1
        for num in nums:
            result *= num
            prefix.append(result)
        
        result = 1
        for num in reversed(nums):
            result *= num
            postfix.append(result)

        for i in range(len(nums)):
            index = len(nums) - i - 2 
            if i == 0:
                output.append(postfix[index])
                continue

            if index <= -1 :
                output.append(prefix[i - 1])
                continue 

            output.append(prefix[i - 1] * postfix[index])

        return output 


        





