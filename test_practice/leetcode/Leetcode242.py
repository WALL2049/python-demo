class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()
        for i in s:
            if i in dict_s.keys():
                dict_s[i] += 1
            else:
                dict_s[i] = 1
        for j in t:
            if j in dict_t.keys():
                dict_t[j] += 1
            else:
                dict_t[j] = 1
        if dict_s == dict_t:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))