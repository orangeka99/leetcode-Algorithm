class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        str_tmp = ""
        for x in range(len(s)):
            match s[x]:
                case "M":
                    if s[x - 1] == "C" and x != 0:
                        result += 800
                    else:
                        result += 1000
                case "D":
                    if s[x - 1] == "C" and x != 0:
                        result += 300
                    else:
                        result += 500
                case "C":
                    if s[x - 1] == "X" and x != 0:
                        result += 80
                    else:
                        result += 100
                case "L":
                    if s[x - 1] == "X" and x != 0:
                        result += 30
                    else:
                        result += 50
                case "X":
                    if s[x - 1] == "I" and x != 0:
                        result += 8
                    else:
                        result += 10
                case "V":
                    if s[x - 1] == "I" and x != 0:
                        result += 3
                    else:
                        result += 5
                case "I":
                    result += 1

        return result
    
arr = "MCMXCIV"
ggg = Solution()
print(ggg.romanToInt(arr))

                
                
                    
                    
            
            
            