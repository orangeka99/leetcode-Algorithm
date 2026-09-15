class Solution:
    def isValid(self, s: str) -> bool:  
        symbol_dic = {
            "(" : 2,
            ")" : 1,
            "{" : 4,
            "}" : 3,
            "[" : 6,
            "]" : 5
        }
        print(len(s))
        if len(s) == 2:
            if symbol_dic.get(s[0]) != symbol_dic.get(s[-1]) + 1:
                return False
            else:
                return True
        if len(s) % 2 != 0:
            return False
        if s[0] == "]" or s[0] == "}" or s[0] == ")":
            return False
        if s[-1] == "{" or s[-1] == "[" or s[-1] == "(":
            return False
        prev_str = []
        for i1 in range(len(s)):
            if i1 == 0:
                prev_str.append(symbol_dic.get(s[i1]))
            else:
                if prev_str == []:
                    prev_str.append(symbol_dic.get(s[i1]))
                    continue
                if prev_str[-1] != symbol_dic.get(s[i1]) + 1:
                    prev_str.append(symbol_dic.get(s[i1]))
                    if len(prev_str) > len(s) / 2:
                        return False
                else:
                    if prev_str != []:
                        prev_str.pop()

        if prev_str == []:
            return True
        else:
            return False
