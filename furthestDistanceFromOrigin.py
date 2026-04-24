class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        countL = 0
        countR = 0
        countUnderScore = 0

        for i in range(len(moves)):

            if moves[i] == "L":
                countL +=1
            
            elif moves[i] == "R":
                countR += 1
            
            else:
                countUnderScore += 1
            
        return abs(countR - countL) + countUnderScore
