class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr_1 = 0
        ptr_2 = len(s) - 1
        while ptr_1 < ptr_2 and ptr_1 <= len(s) - 1 :
            while not s[ptr_1].isalnum():
                ptr_1 += 1 
                if ptr_1 > len(s) - 1:
                    break
            
            while not s[ptr_2].isalnum():
                ptr_2 -= 1 
                if ptr_2 < 0:
                    break

            if ptr_1 < ptr_2 and ptr_1 <= len(s) - 1:
                if s[ptr_1].lower() != s[ptr_2].lower():
                    return False
            else:
                break 

            ptr_1 += 1
            ptr_2 -= 1 

        return True 
        