class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 1:
            return [char for char in phone_dict.get(digits[0])]
        
        result = []
        tmp_arr = []
        for i1 in range(len(digits[1:])):
            dic_str = phone_dict.get(digits[1:][i1])
            if i1 == 0:
                for i2 in range(len(phone_dict.get(digits[0]))):
                    for i3 in range(len(dic_str)):
                        result.append(phone_dict.get(digits[0])[i2] + dic_str[i3])
            else:
                tmp_arr = []
                for i2 in range(len(result)):
                    for i3 in range(len(dic_str)):
                        tmp_arr.append(result[i2] + dic_str[i3])
                
                result = tmp_arr
        
        return result

strr2 = digits = "99"
ggg = Solution()
print(ggg.letterCombinations(strr2))
                        
                


                        
                            
    