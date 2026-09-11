import math as m
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        main_arr = sorted(nums)
        main_len = len(main_arr)
        if target <= main_arr[0]:
            if main_arr[0] + main_arr[1] + main_arr[2] > target:
                return main_arr[0] + main_arr[1] + main_arr[2]

        if target > main_arr[main_len - 1]:
            if main_arr[main_len - 1] + main_arr[main_len - 2] + main_arr[main_len - 3] < target:
                return main_arr[main_len - 1] + main_arr[main_len - 2] + main_arr[main_len - 3]
        prev_arr = []
        
        val_list = [target - 1,target + 1, target]
        current_val = 0
        val_len = 0
        for i1 in range(main_len):
            for i2 in range(i1 + 1,main_len):
                for i3 in range(len(val_list)):
                    if prev_arr != []:
                        if prev_arr[0] == target:
                            break
                    current_val = main_arr[i1] + main_arr[i2] - val_list[i3]                    
                    current_val *= -1                    
                    if current_val in main_arr:
                        index = main_arr.index(current_val)
                        if index == i1 or index == i2:
                            continue
                        total = main_arr[i1] + main_arr[i2] + current_val
                        if val_list[i3] < total:
                            val_len = len(range(val_list[i3], total))
                        elif val_list[i3] >= total:
                            val_len = len(range(total, val_list[i3]))
                        else:
                            val_len = 0
                        if prev_arr == []:
                            prev_arr.append(total)
                            prev_arr.append(val_len)
                            
                        else:
                            if total == target:
                                prev_arr[0] = total
                                prev_arr[1] = val_len
                            else:
                                if prev_arr[1] >= val_len:
                                    prev_arr[0] = total
                                    prev_arr[1] = val_len
        
        if prev_arr != []:
            return prev_arr[0]
        else:
            current_val = 0
            val_len = 0
            for i1 in range(main_len - 2):
                for i2 in range(i1 + 1,main_len):
                    for i3 in range(i2 + 1,main_len):
                        current_val = main_arr[i1] + main_arr[i2] + main_arr[i3]
                        if current_val < target:
                            val_len = len(range(current_val,target))
                        else:
                            val_len = len(range(target, current_val))
                        
                        if i1 == 0 and i2 == 1 and i3 == 2:
                            prev_arr.append(current_val)
                            prev_arr.append(val_len)
                        else:
                            if val_len < prev_arr[1]:
                                prev_arr[0] = current_val
                                prev_arr[1] = val_len
            return prev_arr[0]
        
arr = [1,2,7,13]
tar = 12
ggg = Solution()
print(ggg.threeSumClosest(arr, tar))



