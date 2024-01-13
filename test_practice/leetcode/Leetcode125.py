# coding=utf-8
"""
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
字母和数字都属于字母数字字符。
给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
"""
import re


class Leetcode125:
    def __init__(self):
        pass

    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        return s1 == s1[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s1 = re.sub("[^a-zA-Z0-9]", "", s).lower()
    print(s1)
    print(s1 == s1[::-1])