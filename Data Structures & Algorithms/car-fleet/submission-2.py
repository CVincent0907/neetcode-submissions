import math 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # reach dest at the same time -> one fleet 
        # cannot surpass the ahead car 
        array = []
        for index, p in enumerate(position):
            array.append((p, speed[index]))

        # Descending order sort by the first element in the tuple, x is the tuple element in the array
        sorted_array = sorted(array,key=lambda x: x[0], reverse=True)

        stack = [] 

        for p,s in sorted_array:
            time = (target - p) / s
            if not stack:
                stack.append(time)
            else: 
                if time > stack[-1]:
                    stack.append(time) 


        return len(stack)

            
            
        
        



