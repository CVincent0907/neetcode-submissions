class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []

        for num in range(len(temperatures)):
            result.append(-1)

        for index, temp in enumerate(temperatures): 
            while stack and temp > stack[-1][1]:
                popout = stack.pop()
                result[popout[0]] = index - popout[0]
            stack.append((index, temp))

        for item in stack:
            result[item[0]] = 0

        return result 


                

                
                
                    
                

