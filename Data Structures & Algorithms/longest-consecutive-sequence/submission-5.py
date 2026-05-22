class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0

        # if len(nums) == 1: 
        #     return 1 

        # table = dict()
        # for num in nums:
        #     table[num] = 1 
        
        # top = None
        # bottom = None 
        # maxLen = 0 
        # length = 1

        # for key in table.keys():
        #     if table.get(key) == 1:
        #         top = key
        #         bottom = key 
        #         while (bottom - 1) in table: #when less than 1 is found 
        #             table[bottom - 1] = 0
        #             length += 1 # len increase by 1 
        #             bottom -= 1 # new bottom to see if exist in the table 

        #         while (top + 1) in table:
        #             table[top + 1] = 0
        #             length += 1 
        #             top += 1 

        #         if length > maxLen:
        #             maxLen = length
                
        #         length = 1
        #         table[key] = 0 
                
        # return maxLen 

        st = set()
        for num in nums:
            st.add(num)

        length = 0
        maxLen = 0

        for num in st:
            if num - 1 not in st: # Identify the starting seq
                length = 1 
                top = num + 1 
                while top in st:
                    length += 1  
                    top += 1 

                if length > maxLen:
                    maxLen = length 
        return maxLen 
                    
            

             

        