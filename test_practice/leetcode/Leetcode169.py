"""
169:����Ԫ��

����һ����СΪ n ������ nums ���������еĶ���Ԫ�ء�����Ԫ����ָ�������г��ִ��� ���� ? n/2 ? ��Ԫ�ء�
����Լ��������Ƿǿյģ����Ҹ������������Ǵ��ڶ���Ԫ�ء�
ʾ�� 1��
���룺nums = [3,2,3]
�����3
ʾ�� 2��
���룺nums = [2,2,1,1,1,2,2]
�����2
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