class Solution(object):
    def findMissingElements(self, nums):
        self.nums = nums
        self.nums.sort()
        self.nums_st = []
        last_no = self.nums[-1]
        first_no = self.nums[0]
        count = first_no
        for i in range(last_no):
            if count not in self.nums:
                self.nums_st.append(count)

            if count == last_no:
                break
            count += 1

        return self.nums_st
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        