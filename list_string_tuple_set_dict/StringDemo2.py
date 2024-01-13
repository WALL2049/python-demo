class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = list(s)
        try:
            for i in t:
                l.remove(i)
            if l == []:
                return True
        except:
            return False


if __name__ == "__main__":
    s = Solution()
    result = s.isAnagram("anagram", "anagrmf")
    print(result)

    firstList = [1, 2, 3, 4]
    secondList = []
    for i in firstList:
        secondList.append(str(i))
    str_first = "".join(secondList)
    print(str_first)

