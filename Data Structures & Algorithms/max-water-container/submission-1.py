class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        ptr1 = 0 
        ptr2 = len(heights) - 1
        area = 0;
        while ptr1 < ptr2:
            width = ptr2 - ptr1
            height = heights[ptr1] if heights[ptr1] <= heights[ptr2] else heights[ptr2] 
            temp = width * height 
            area = temp if temp > area else area 

            if heights[ptr1] < heights[ptr2]:
                ptr1 += 1
            else: 
                ptr2 -= 1  
        return area 

        

