class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        wordList.append(endWord)

        adj = defaultdict(list)

        for word in wordList:

            for i in range(len(word)):

                pattern = word[:i] + "*" + word[i+1:]

                adj[pattern].append(word)
        
        res = 1
        queue = []
        visit = set()

        queue.append(beginWord)
        visit.add(beginWord)

        while queue:

            for i in range(len(queue)):
            
                node = queue.pop(0)

                if node == endWord:
                    return res
                
                for i in range(len(node)):

                    pattern = node[:i] + "*" + node[i+1:]
                
                    for nei in adj[pattern]:

                        if nei not in visit:

                            queue.append(nei)

                            visit.add(nei)
                
            res += 1
        
        return 0









            
