
# 创建前缀树类
class Trie():
    # 定义前缀树开始为空
    def __init__(self):
        self.dict = {}
    # 定义嵌入word功能，并以{'#':word}结尾
    def insert(self, word):
        node = self.dict
        for w in word:
            if w not in node:
                node[w]= {}
            node = node[w]
        node['#'] = word
# 生成words的前缀树
words = ['food', 'foot', 'rat', 'wet']
a = Trie()
for word in words:
    a.insert(word)
trie = a.dict
print(trie)
#
# 创建解题方法类
class Solution(object):
    def findWords(self, board, words):
        res = []
        # trie = Trie()
        # node = trie.root
        # for w in words:
        #     trie.insert(w)

        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp_state = []
                self.dfs(i, j, board, tmp_state, trie, res)
        return res

    def dfs(self, i, j, board, tmp_state, trie, res):
        if '#' in trie and tire['#'] not in res:
            res.append(trie['#'])
        if [i, j] not in tmp_state and board[i][j] in trie:
            tmp = tmp_state + [[i, j]]
            candidate = []
            if i - 1 >= 0:
                candidate.append([i - 1, j])
            if i + 1 < len(board):
                candidate.append([i + 1, j])
            if j - 1 >= 0:
                candidate.append([i, j - 1])
            if j + 1 < len(board[0]):
                candidate.append([i, j + 1])
            trie = trie[board[i][j]]
            if '#' in trie and trie['#'] not in res:
                res.append(trie['#'])
            for item in candidate:
                self.dfs(item[0], item[1], board, tmp, trie, res)

