class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
            else:
                if target % 2 == 1:
                    target -= 1
                else:
                    if maxDoubles > 0:
                        target //= 2
                        maxDoubles -= 1
                    else:
                        moves += target - 1
                        break
            moves += 1
        return moves
