class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        self.output = []
        length = len(self.nums)
        counting = 0
        check = 0
        for i in range(len(self.nums)):
            for x in range(len(self.nums)):
                if i != x:
                    if self.nums[i] + self.nums[x] == target:
                        self.output.append(i)
                        self.output.append(x)
                        check = 1
                        break
            
            if check == 1:
                break

        return self.output
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        