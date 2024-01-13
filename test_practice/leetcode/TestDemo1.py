class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict = dict()
        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        list_keys = list(count_dict.keys())
        list_values = list(count_dict.values())
        max_index = 0
        for i in range(1, len(list_values)):
            if list_values[i] > list_values[max_index]:
                max_index= i
        return list_keys[max_index]

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))