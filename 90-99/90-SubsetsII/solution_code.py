from typing import List
import copy
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []          # 放入空集
        cur_subset = []
        self.appendSubsets(0, cur_subset, nums, result)
        return result
        
                
    def appendSubsets(self, i, cur, nums, res):
        res.append(cur)      # 将集合cur加入res中
        # 将每个元素都添加进res中的每个集合
        for j in range(i, len(nums)):
            # 如果nums[j]与前一个相同，跳过
            if j > i and nums[j] == nums[j-1]:
                continue
            # 集合cur变长后进行递归
            self.appendSubsets(j+1, cur+[nums[j]],nums, res)