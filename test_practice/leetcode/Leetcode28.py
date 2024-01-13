"""
 ���������ַ��� haystack �� needle �������� haystack �ַ������ҳ� needle �ַ����ĵ�һ��ƥ������±꣨�±�� 0 ��ʼ������� needle ���� haystack ��һ���֣��򷵻�  -1 ��
 ʾ�� 1��
 ���룺haystack = "sadbutsad", needle = "sad"
 �����0
 ���ͣ�"sad" ���±� 0 �� 6 ��ƥ�䡣
 ��һ��ƥ������±��� 0 �����Է��� 0 ��
 ʾ�� 2��
 ���룺haystack = "leetcode", needle = "leeto"
 �����-1
 ���ͣ�"leeto" û���� "leetcode" �г��֣����Է��� -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            found = True
            for j in range(n):
                if haystack[i+j] != needle[j]:
                    found = False
                    break
            if found:
                return i
        return -1