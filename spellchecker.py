
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def to_lower(s):
            return s.lower()

        def mask_vowels(s):
            return "".join('*' if c in "aeiou" else c for c in s.lower())

        # Exact words
        exact = set(wordlist)

        # First lowercase match
        case_map = {}
        for w in wordlist:
            lw = to_lower(w)
            if lw not in case_map:
                case_map[lw] = w

        # First vowel-masked match
        vowel_map = {}
        for w in wordlist:
            mw = mask_vowels(w)
            if mw not in vowel_map:
                vowel_map[mw] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            elif to_lower(q) in case_map:
                ans.append(case_map[to_lower(q)])
            elif mask_vowels(q) in vowel_map:
                ans.append(vowel_map[mask_vowels(q)])
            else:
                ans.append("")
        return ans
