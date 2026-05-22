class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0 

        for index, h in enumerate(height):
            if index == 0:
                maxLeft = 0
            else:
                maxLeft = max(height[0:index])

            if index == len(height)-1:
                maxRight = 0
            else:
                maxRight = max(height[index+1:len(height)])
            
            # Must account for the fact that current h is the largest and nothing is trapped at index where h is 
            area = max(0, min(maxRight, maxLeft) - h) 
            totalArea += area

        return totalArea 