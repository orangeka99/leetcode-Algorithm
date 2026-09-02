import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.findall(p, s)
        if (result == []):
            return False
        if (result[0] != s):
            return False
        else:
            return True 