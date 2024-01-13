class Solution:

    @staticmethod
    def quick_sort(alist):
        if len(alist) >= 2:
            left = list()
            right = list()
            base = alist[0]
            alist.remove(base)
            for element in alist:
                if element <= base:
                    left.append(element)
                else:
                    right.append(element)

            return Solution.quick_sort(left) + [base] + Solution.quick_sort(right)
        else:
            return alist

if __name__ == '__main__':
    alist = [4, 84, 3, 7, 38, 19, 12, 97, 88, 53, 42, 73, 10, 46, 4, 29, 73]
    print(Solution.quick_sort(alist))


