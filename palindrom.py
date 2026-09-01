import math as mm
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        arr_main = str(x)
        main_len = len(arr_main)
        half_len = mm.ceil(main_len/2)
        left_text = ""
        right_text = ""
        
        if main_len % 2 == 0:
            left_text = arr_main[0:half_len]
            right_text = arr_main[half_len:main_len]
        else:
            left_text = arr_main[0:half_len - 1]
            right_text = arr_main[half_len:main_len]
        right_text = right_text[::-1]
        
        if left_text == right_text:
            return True
        else:
            return False
    

numm = 10
gggg = Solution()
print(gggg.isPalindrome(numm))

# 121 1221 12521 5,3 12344321 8,4