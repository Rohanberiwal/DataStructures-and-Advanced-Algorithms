class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,i,j,count,word):
            if(count == len(word)):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or word[count]!=board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = ""
            found = dfs(board,i+1,j,count+1,word) or dfs(board,i-1,j,count+1,word) or dfs(board,i,j+1,count+1,word) or dfs(board,i,j-1,count+1,word)
            board[i][j] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(board,i,j,0,word):
                    return True
        return False
