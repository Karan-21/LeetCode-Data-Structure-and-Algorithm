class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = initialBoxes.copy() # boxes to travel to
        foundKeys = set(initialBoxes) # keys we have found so far
        traveled = set() # boxes that have been traveled to so far. If a box is in this set, it means this box is reachable. Also this can be used to avoid cycles(although no cycles in this problem)

        while queue:
            size = len(queue)

            for _ in range(size):
                index = queue.pop(0)

                for boxIndex in containedBoxes[index]: # for every box inside this box
                    if boxIndex not in traveled:
                        queue.append(boxIndex) # travel to this box later

                foundKeys.update(keys[index]) # gather the keys we found in this box
                traveled.add(index) # mark that this box has been traveled to and is reachable

        return sum(candies[i] for i in traveled if status[i] == 1 or i in foundKeys) # gather all candies from reachable boxes that are open already, or can be opened with a key
