class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = set()
        placed = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j] and j not in used:
                    used.add(j)
                    placed+=1
                    break
        return len(fruits)-placed
        
