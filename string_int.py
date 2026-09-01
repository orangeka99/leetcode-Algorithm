import numbers
class Solution:
    def myAtoi(self, s: str) -> int:
        str_main = s.strip()
        str_main = list(str_main)
        sign_arr = ["-","+"]
        nums_str = ["1","2","3","4","5","6","7","8","9","0"]
        
        if str_main == []:
            return 0
        
        if str_main[0] not in sign_arr:
            if str_main[0] not in nums_str:
                return 0

        str_result = []
        check_zero = False
        for i in range(len(str_main)):
                if i == 0:
                    if str_main[i] in nums_str:
                        check_zero = True
                    str_result.append(str_main[i])
                else:
                    if str_main[i] not in nums_str:
                        break
                    if str_main[i] in sign_arr:
                        break
                
                    str_result.append(str_main[i])
                    if str_main[i] == "0":
                        if len(str_result) == 1:
                            continue
                        if check_zero == False:
                            str_result.pop()
                    else:
                        check_zero = True
        
        if len(str_result) == 1 and str_result[0] in sign_arr:
            return 0
        
        if len(str_result) > 1 and str_result[0] == "0": # check leading zero
                str_result.pop(0)
        
        if str_result[0] in sign_arr and len(str_result) >= 2 and str_result[1] == "0":
            return 0
        else:
            numbs_re = 0
            check_neg = False
            if str_result[0] in sign_arr:
                if str_result[0] == "-":
                    check_neg = True
                str_result.pop(0)
            for x in range(len(str_result)):
                if (x == 0):
                    numbs_re = int(str_result[x])
                else:
                    numbs_re = (numbs_re * 10) + int(str_result[x])
                    
            if (-2**31 <= numbs_re < 2**31) == False:
                numbs_re = 2**31
                if check_neg == True:
                    numbs_re *= -1
                else:
                    numbs_re -= 1
            else:
                if check_neg == True:
                    numbs_re *= -1
            return numbs_re
                


test = Solution()
str_test = "42"
print(test.myAtoi(str_test))

# test_tt = "-4"
# nmb = int(test_tt)
# print(nmb)