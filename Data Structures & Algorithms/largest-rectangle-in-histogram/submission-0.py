class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_area = float('-inf')

        for index, h in enumerate(heights):
            if not stack:
                stack.append((index, h))
            else:
                if h >= stack[-1][1]:
                    stack.append((index,h))
                else: 
                    last_pop_index = index 
                    while stack and h < stack[-1][1]:
                        largest_area = max(largest_area, (index-stack[-1][0])*stack[-1][1])
                        last_pop_index = stack.pop()[0]

                    stack.append((last_pop_index, h))
        
        while stack:
            largest_area = max(largest_area,(len(heights)-stack[-1][0])*stack[-1][1])
            stack.pop()
        
        return largest_area
                    


                