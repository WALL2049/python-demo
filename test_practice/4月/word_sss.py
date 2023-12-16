class Solution:
    def findWords(self, board, words):
        # 如果输入为空，返回空值
        if not board or not board[0] or not words:
            return []
        # 创建前缀树trie，表示为self.root，以{'#':word}结尾。节点为node
        self.root = {}
        for word in words:
            node = self.root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word
        # 对board进行深度优先搜索
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                tmp_state = []
                self.dfs(i, j, board, tmp_state, self.root, res)
        return res
    # 定义DFS
    def dfs(self, i, j, board, tmp_state, node, res):
        # if '#' in node and node['#'] not in res:
        #     res.append(node['#'])
        # 如果字母的坐标未被记录，且该字母出现在单词中（前缀树的节点中），则记录它
        if [i, j] not in tmp_state and board[i][j] in node:
            tmp = tmp_state + [[i, j]]
            # 不超出board范围的坐标都在搜索名单，左右上下依次搜索
            candidate = []
            if i - 1 >= 0:
                candidate.append([i - 1, j])
            if i + 1 < len(board):
                candidate.append([i + 1, j])
            if j - 1 >= 0:
                candidate.append([i, j - 1])
            if j + 1 < len(board[0]):
                candidate.append([i, j + 1])
            # 如果node中有该字母，判断有没有到最后， 如果#前的字母都验证正确且该单词未被加入res，则加入
            node = node[board[i][j]]
            if '#' in node and node['#'] not in res:
                res.append(node['#'])
            # 对所有候选搜索元素进行深度优先搜索，从近邻的开始判断
            for item in candidate:
                self.dfs(item[0], item[1], board, tmp, node, res)

