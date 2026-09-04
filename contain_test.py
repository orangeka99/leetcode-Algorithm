import math as m
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_arr = []
        right_arr = []
        height_len = len(height)
        max_val = 0
        left_avg = 0
        right_avg = 0
        if height_len % 2 == 0: # even Number
            left_arr = height[0:int(height_len / 2)]
            right_arr = height[int(height_len / 2): height_len]
        else:
            left_arr = height[0:m.ceil(height_len / 2)]
            right_arr = height[m.ceil(height_len / 2): height_len]

        if height_len > 500:        
            left_avg = m.floor(sum(left_arr) / len(left_arr))
            right_avg = m.floor(sum(right_arr) / len(right_arr))

        print(left_avg)
        print(right_avg)
        print(max(left_arr))
        print(max(right_arr))
        for x in range(len(left_arr)):
            if left_arr[x] < left_avg:
                continue
            for i in range(len(right_arr)):
                #fleft side to right side
                if right_arr[i] < right_avg:
                    continue
                if left_arr[x] != right_arr[i]: 
                    if left_arr[x] < right_arr[i]:
                        y_val = left_arr[x]
                    else:
                        y_val = right_arr[i]
                else:
                    y_val = left_arr[x]
                x_val = ( len(left_arr) - x ) + i
                sum1 =  y_val * x_val
                if max_val < sum1:
                    max_val = sum1
                    
                #left side
                if x != i:
                    if left_arr[x] != left_arr[i]: 
                        if left_arr[x] < left_arr[i]:
                            y_val = left_arr[x]
                        else:
                            y_val = left_arr[i]
                    else:
                        y_val = left_arr[x]
                    x_val = abs(x - i)
                    sum1 =  y_val * x_val
                    if max_val < sum1:
                        max_val = sum1
                
                #right side
                if x != len(right_arr):
                    if x != i:
                        if right_arr[x] != right_arr[i]: 
                            if right_arr[x] < right_arr[i]:
                                y_val = right_arr[x]
                            else:
                                y_val = right_arr[i]
                        else:
                            y_val = right_arr[x]
                        x_val = abs(x - i)
                        sum1=  y_val * x_val
                        if max_val < sum1:
                            max_val = sum1
                        
        return max_val
