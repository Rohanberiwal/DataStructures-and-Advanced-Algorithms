class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        max_score = 0
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score


"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        if score == 0 :
            for i in tokens  :
                if i <= power :
                    power  = power - i 
                    score = score + 1
        elif score > 0  :
            max_finder =  max(tokens)
            score = score -1
            sum_finder  = 0 
            power = power + max_finder 
            for i in token :
                if i < power  :
                    score = score +1
        return score 
"""
