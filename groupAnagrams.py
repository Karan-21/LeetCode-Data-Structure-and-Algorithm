class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}

        for i in strs:

            word = "".join(sorted(i))

            if word not in dict:
                dict[word] = [i]
            
            else:
                dict[word].append(i)
        
        return dict.values()
