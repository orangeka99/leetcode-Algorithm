class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if strs == [""] or strs == []:
            return result
        if len(strs) == 1:
            return strs[0]
        string_min = min(strs, key=len)
        string_main = sorted(strs, key=len)
        string_len = len(string_main)
        
        for x in range(len(string_min)):
            character = [word[x] for word in strs]
            if len(character) != len(set(character)) == True:
                result += character[0]
            else:
                break
        
        return result


str_t = ["flower","flow","flight"]
ggg = Solution()
print(ggg.longestCommonPrefix(str_t))