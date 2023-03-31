class Solution:

    class TrieNode:
        def __init__(self) -> None:
            self.children = [None for _ in range(26)]
            self.counter = 0
            self.s = None  # For a leaf trie node x, we will set x.s as the word it represents

        def __str__(self) -> str:
            ss = "counter=" + str(self.counter) + ", "
            if self.s is not None:
                ss += "s=" + self.s + ", "
            ss += "("
            for i in range(len(self.children)):
                child = self.children[i]
                if child is not None:
                    ss += chr(i + ord('a')) + ": "
                    ss += str(child)
            ss += ")"
            return ss
            
    class Trie:
        def __init__(self) -> None:
            self.root = Solution.TrieNode()
        
        def insert(self, s) -> None:
            curr_node = self.root
            curr_node.counter += 1
            for c in s:
                i = ord(c) - ord('a')
                if curr_node.children[i] is None:
                    curr_node.children[i] = Solution.TrieNode()
                curr_node = curr_node.children[i]
                curr_node.counter += 1
            curr_node.s = s

    def search(self, i: int, j: int, board: List[List[str]], visited: List[List[bool]], node : TrieNode, res: List[str]) -> bool:

        if node is None or node.counter <= 0 or visited[i][j]:
            return False
        
        search_res = False
        if node.s is not None:
            res.append(node.s)
            node.counter -= 1
            node.s = None  # clear the string
            search_res = True # got a string, but we will also go through the current char to explore longer strings
                                # E.g. got "snow" but there might exist "snowy" so we won't stop here

        directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        visited[i][j] = True
        search_res_count = 0
        for direct in directs:
            next_i = i + direct[0]
            next_j = j + direct[1]
            if next_i >= 0 and next_j >= 0 and next_i < len(board) and next_j < len(board[0]):
                # search_res = self.search(next_i, next_j, board, visited, node.children[ord(board[next_i][next_j]) - ord('a')], res) or search_res
                if self.search(next_i, next_j, board, visited, node.children[ord(board[next_i][next_j]) - ord('a')], res):
                    search_res_count += 1 
        search_res = True if search_res_count > 0 else search_res
        if search_res:  # note
            node.counter -= search_res_count
        visited[i][j] = False
        return search_res


    # Slower version: remove return value (remove functionality of TrieNode counter)
    # def search(self, i: int, j: int, board: List[List[str]], visited: List[List[bool]], node : TrieNode, res: List[str]) -> None:

    #     if node is None or visited[i][j]:
    #         return
    #     if node.s is not None:
    #         res.append(node.s)
    #         node.counter -= 1
    #         node.s = None  # clear the string

    #     directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    #     visited[i][j] = True
    #     for direct in directs:
    #         next_i = i + direct[0]
    #         next_j = j + direct[1]
    #         if next_i >= 0 and next_j >= 0 and next_i < len(board) and next_j < len(board[0]):
    #             # search_res = self.search(next_i, next_j, board, visited, node.children[ord(board[next_i][next_j]) - ord('a')], res) or search_res
    #             self.search(next_i, next_j, board, visited, node.children[ord(board[next_i][next_j]) - ord('a')], res)
    #     visited[i][j] = False



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        T = self.Trie()
        for word in words:
            T.insert(word)

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = []
        for i in range(m):
            for j in range(n):
                self.search(i, j, board, visited, T.root.children[ord(board[i][j]) - ord('a')], res)
        
        return res
