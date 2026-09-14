class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        main_arr = sorted(nums)
                
        if len(main_arr) < 4:
            return []
        
        if len(main_arr) == 4:
            if main_arr[0] + main_arr[1] + main_arr[2] + main_arr[3] != target:
                return []
            else:
                return [[main_arr[0], main_arr[1], main_arr[2],main_arr[3]]]
             
        unique_numbers = list(dict.fromkeys(nums))

        if len(unique_numbers) == 1 and len(main_arr) != 1:
            return [[unique_numbers[0], unique_numbers[0], unique_numbers[0],unique_numbers[0]]]
        
        check_bet = ""
        if target < 0:
            if main_arr[0] > target:
                check_bet = "more_zero"
        else:
            if main_arr[-1] < target:
                main_arr = sorted(nums, reverse=True)
                check_bet = "less_zero"
                
        my_set = set(main_arr)
        print(my_set)
        print(main_arr)
        unique_rows = set()
        tmp_arr = []

        for i1 in range(len(main_arr)):                
            for i2 in range(i1 + 1,len(main_arr)):
                for i3 in range(i2 + 1, len(main_arr)):
                    current_val = main_arr[i1] + main_arr[i2] + main_arr[i3]
                    if check_bet == "more_zero":
                        if current_val > 0:
                            break
                    elif check_bet == "less_zero":
                        if current_val < 0:
                            break
                    current_val = current_val - target
                    current_val *= -1
                    if current_val in my_set:
                        index = main_arr.index(current_val)
                        if index == i1 or index == i2 or index == i3:
                            continue
                    else:
                        continue

                    tmp_arr.append(main_arr[i1])
                    tmp_arr.append(main_arr[i2])
                    tmp_arr.append(main_arr[i3])
                    tmp_arr.append(current_val)
                    tmp_arr.sort()
                    my_s = set(tmp_arr)
                    
                    if my_s in unique_rows:
                        tmp_arr = []
                        continue
                    unique_rows.add(tuple(tmp_arr))
                    my_s.clear()
                    tmp_arr = []   
        
        result: list[list[int]] = [[]]
        result = [list(item) for item in unique_rows]
        return result