class Solution:
    def asteroidsDestroyed(self, m: int, a: List[int]) -> bool:
        return all(accumulate([m]+sorted(a),lambda q,v:q>=v and q+v))
