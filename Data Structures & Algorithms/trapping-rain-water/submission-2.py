class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        leftPtr = 0
        rightPtr = len(height) - 1 
        maxL = height[leftPtr]
        maxR = height[rightPtr]
        
        while leftPtr < rightPtr:
            if maxL <= maxR:
                leftPtr += 1
                totalArea += max(0, maxL-height[leftPtr])
                maxL = max(maxL, height[leftPtr])
            else:
                rightPtr -= 1
                totalArea += max(0, maxR - height[rightPtr])
                maxR = max(maxR, height[rightPtr])
                
        return totalArea
            