class Solution:
    def convert(self, s: str, numRows: int) -> str:
        __str = s
        __str_sec = s
        __str_thrd = s
        __str_store = []
        __rows = numRows
        __tmp_store = str()
        __str_real = str()
        __cont = 3
        
        #constant value
        __num = abs(__cont - __rows)
        __cc = __num * 2
        __main_cont = 4 + __cc
        
        #second loop length
        #__sec_loop = int(len(__str) / __rows) + 3
        __sec_loop = int(len(__str) / 2)
        print(len(__str))
        #if __sec_loop < 10:
        #    __sec_loop = 10
            
        if __rows == 2:
            __sec_loop += 3
            __main_cont = 2
            
        __going_first_num = __main_cont
        __going_sec_num = 0
        __x_count = 0
        __first_tmp = __main_cont
        
        __str_len = len(__str)
        if __str_len < __rows or __rows == 1:
            return __str 
        
        for __i in range(__rows):
            for __x in range(__sec_loop):
                __x_count += 1
                if __x == 0:
                    __tmp_store = __tmp_store + __str[__i]
                else:
                    if __i == 0 or __i == int(__rows - 1) or __rows == 2:
                        __tmp_store = __tmp_store + __str_sec[__first_tmp:__first_tmp + 1]
                        __str_sec = __str_sec[__first_tmp:len(__str_sec)]
                    else:
                        if __x_count % 2 == 0: #even number
                            __tmp_store = __tmp_store + __str_sec[__going_first_num:__going_first_num + 1]
                            __str_sec = __str_sec[__going_first_num:len(__str_sec)]
                        else: # odd number
                            __tmp_store = __tmp_store + __str_sec[__going_sec_num:__going_sec_num + 1]
                            __str_sec = __str_sec[__going_sec_num:len(__str_sec)]
                            
                
            __x_count = 0

            __str_store.append(__tmp_store)
            __str_real = __str_real + __tmp_store
            __str_thrd = __str_thrd[1:int(len(__str_thrd))]
            __going_first_num = __going_first_num - 2
            __going_sec_num = __main_cont - __going_first_num
            __tmp_store = ""
            __first_tmp = __main_cont
            __str_sec = __str_thrd

        return __str_real