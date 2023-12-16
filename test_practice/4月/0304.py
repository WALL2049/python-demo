#
# class Trie:
#
#     def __init__(self):
#
#         self.root = {}
#         self.word_end = -1
#
#     def insert(self, word):
#
#         t = self.root
#         for w in word:
#             if w not in t:
#                 t[w] = {}
#             t = t[w]
#
#         curNode[self.word_end] = True

# words = ['cad', 'car', 'and']
# trie = {}
# i = 0
# for word in words:
#     print(f'前{i}个单词存入后的前缀树：{trie}')
#     t = trie
#     for w in word:
#         if w not in t:
#             t[w] = {}
#         t = t[w]
#     t['end'] = 1
#     i += 1
# print("所有单词存入后的前缀树：", trie)

words = ['food', 'foot', 'rat', 'wet']

root = {}
for word in words:
   node = root
   for char in word:
       if char not in node:

           node[char] = {}
       node = node[char]
   node['#'] = word

print(root)