class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        __nums1 = nums1
        __nums2 = nums2
        
        __sum = float()
        
        __pos = 0
        
        __num_merge = __nums1 + __nums2
        __num_merge.sort()
        __num_len = len(__num_merge)
        
        print(__num_merge)
        
        if __num_len == 1:
            __sum = __num_merge[0]
            return __sum
        
        #for __i in range(__num_len):
         #   __sum += __num_merge[__i]

        #find median
        __pos = int(__num_len / 2)
        if __num_len % 2 == 0: # even no
            #__pos = int(__num_len / 2)
            __posf = __pos - 1
            __poss = __pos

            __sum = float((__num_merge[__posf] + __num_merge[__poss]) / 2)
        else: # Odd no
            #__pos = int(__num_len / 2)

            __sum = float(__num_merge[__pos])           
        return __sum