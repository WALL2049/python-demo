"""
169:多数元素

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ? n/2 ? 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：nums = [3,2,3]
输出：3
示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = dict()
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        list_keys = list(count_dict.keys())
        list_values = list(count_dict.values())
        # max_index = 0
        # for i in range(1, len(list_values)):
        #     if list_values[i] > list_values[max_index]:
        #         max_index= i
        # return list_keys[max_index]
        max_value = list_values[0]
        for value in list_values:
            if value > max_value:
                max_value = value
        return list_keys[list_values.index(max_value)]