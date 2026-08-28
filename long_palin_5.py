class Solution:        
    def longestPalindrome(self, s: str) -> str:
        __str = s
        __tmp_str = str()
        __tmp_store = []
        __sec_str = s
        if len(__str) == 1:
            return __str
        elif __str is None:
            return __str

        for __i in range(len(__str)):
            __tmp_str = __str[__i]
            __sec_len = len(__sec_str)
            __sec_str = __sec_str[1:__sec_len]
            for __x in range(len(__sec_str)):
                __tmp_str = __tmp_str + __sec_str[__x]
                __tmp_len = len(__tmp_str)
                if __tmp_len % 2 == 0: #even number
                    if __tmp_str[0] == __tmp_str[__tmp_len - 1]:
                        __even_len = len(__tmp_str)
                        __even_first = __tmp_str[0]
                        __even_last = __tmp_str[__even_len - 1]
                        __even_left = __tmp_str[1:int(__even_len / 2)]
                        __even_right = __tmp_str[int(__even_len / 2):__even_len - 1]
                        __even_right = __even_right[::-1]
                        if __even_left == __even_right:
                            __tmp_store.append(__tmp_str)           
                else:# odd umber
                    __odd_len = len(__tmp_str)
                    __str_first = __tmp_str[0]
                    __str_last = __tmp_str[__odd_len - 1]
                    if __str_first == __str_last:
                        __str_btw = __tmp_str[1:__odd_len - 1]
                        __str_btw_len = len(__tmp_str)
                        __str_mid_pos = int(len(__str_btw) / 2)
                        __str_right_rev = __str_btw[__str_mid_pos + 1:__str_btw_len]
                        __str_right_rev = __str_right_rev[::-1]
                        if __str_btw[0:__str_mid_pos] == __str_right_rev:
                            __tmp_store.append(__tmp_str)
        if __tmp_store == []:
            __ggg = __str[0]
            return __ggg
        else:
            __longest = sorted(__tmp_store, key=len, reverse=True)
            __long_str = __longest[0]                                                   
            return __long_str