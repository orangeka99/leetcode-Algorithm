class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums_arr = sorted(nums)
        unique_numbers = list(dict.fromkeys(nums))
        # print(unique_numbers)
        if len(unique_numbers) == 1:
            if unique_numbers[0] == 0:
                ret = [[unique_numbers[0], unique_numbers[0], unique_numbers[0]]]
                return ret
        
        my_set = set(nums_arr)
        
        sum_ij = 0
        result: list[list[int]] = [[]]
        unique_rows = set()
        nums_tmp = []
        tmp_res = []
        for i in range(len(nums_arr)):
            if nums_arr[i] > 0:
                break
            if nums_tmp == []:# check -1,-1,-1,0,0,0,1,1,1
                nums_tmp.append(nums_arr[i])
                nums_tmp.append(1)
            else:
                if nums_tmp[0] != nums_arr[i]:
                    nums_tmp = []
                    nums_tmp.append(nums_arr[i])
                    nums_tmp.append(1)
                else:
                    if nums_tmp[0] == nums_arr[i]:
                        if nums_tmp[1] == 2:
                            continue
                        else:
                            nums_tmp[1] += 1
            for x in range(i + 1,len(nums_arr)):
                sum_ij = nums_arr[i] + nums_arr[x]
                if sum_ij <= 0:
                    sum_ij = sum_ij * -1
                else:
                    continue
                if sum_ij in my_set:
                    index = nums_arr.index(sum_ij)
                    if index == i or index == x:
                        continue
                else:
                    continue
                tmp_res.append(nums_arr[i])
                tmp_res.append(nums_arr[x])
                tmp_res.append(sum_ij)
                tmp_res.sort()
                my_s = set(tmp_res)
                
                if my_s in unique_rows:
                    tmp_res = []
                    continue
                unique_rows.add(tuple(tmp_res))
                my_s.clear()
                tmp_res = []
        result = [list(item) for item in unique_rows]
        return result

arr = [1,2,0,1,0,0,0,0]
# arr = [-100,-70,-60,110,120,130,160]
# arr = [-1,0,1,2,-1,-4]
ggg = Solution()
print(ggg.threeSum(arr))