 def maxDepthAfterSplit(self, s: str) -> List[int]:
    return [i&1^(c=='(') for i,c in enumerate(s)]
