class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num)
        length = len(str(abs(num)))
        num_loop = 0
        str_res = ""
        str_tmp = ""
        for x in range(length):
            num_loop = int(num_str[0])
            match len(num_str):
                case 4:
                    for i in range(num_loop):
                        str_tmp += "M"                  
                case 3:
                    for i in range(num_loop):
                        str_tmp += "C"
                        if i == 3:
                            str_tmp = "CD"
                        if i == 4:
                            str_tmp = "D"
                        elif i == 8:
                            str_tmp = "CM"
                case 2:
                    for i in range(num_loop):
                        str_tmp += "X"
                        if i == 3:
                            str_tmp = "XL"
                        if i == 4:
                            str_tmp = "L"
                        elif i == 8:
                            str_tmp = "XC"
                case 1:
                    for i in range(num_loop):
                        str_tmp += "I"
                        if i == 3:
                            str_tmp = "IV"
                        elif i == 4:
                            str_tmp = "V"
                        elif i == 8:
                            str_tmp = "IX"
            str_res += str_tmp
            str_tmp = ""
            num_str = num_str[1:]
            
        
        return str_res
    
ggg = 3749
sss = Solution()
print(sss.intToRoman(ggg))
            
            
            