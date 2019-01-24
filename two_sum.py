def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        total_n = len(nums)
        for n in range(total_n):
            sub_num = target - nums[n]
            for m in range(n+1, len(nums)):
                if nums[m] == sub_num:
                    return [n, m]