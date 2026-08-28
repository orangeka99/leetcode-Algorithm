class Solution(object):
    def lengthOfLongestSubstring(self, s):
        __str = s
        __str_store = []
        __str_len = 0
        __number = []
        __pos = 0
        __st_pos = 0

        for __i in range(len(__str)):
            if __i == 0:
                __str_store.append(__str[__i])
            elif __str[__i] not in __str_store:
                __str_store.append(__str[__i])
            else:

                for __x in range(len(__str_store)):
                    
                    if __str_store[__x] == __str[__i]:
                        __pos = __x
                        break
                
                __str_len = len(__str_store)
                __number.append(__str_len)

                __str_store = __str_store[__pos + 1:__str_len]

                __str_store.append(__str[__i])
                __str_len = 0
        
        if __str_store != []:
            __str_len = len(__str_store)
            __number.append(__str_len)

        if __number != []:
            __number.sort()
            __number = list(dict.fromkeys(__number))
            __max = __number[-1]
            return __max
        else:
            return 0