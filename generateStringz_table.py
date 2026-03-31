def z_table(s):
    n = len(s)
    z = [0] * n
    L = R = 0
    for i in range(1, n):
        if i < R:
            k = i - L
            if z[k] + i < R:
                z[i] = z[k]
                continue
            L = i
        else:
            L = R = i
        while R < n and s[R - L] == s[R]:
            R += 1
        z[i] = R - L
    return z

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        z = z_table(str2)
        ans = ['*'] * (n + m - 1)
        prev = -m
        for i, tf in enumerate(str1):
            if tf == 'T':
                diff = i - prev
                if diff < m:
                    if z[diff] == m - diff:
                        ans[prev + m:i + m] = str2[-diff:]
                    else:
                        return ''
                else:
                    ans[i:i + m] = str2
                prev = i
        l = list(str2) + ['$'] + ans
        wild = set()
        last = None
        for i in range(m + 1, len(l)):
            if l[i] == '*':
                l[i] = 'a'
                wild.add(i)
                if i < 2 * m + 1:
                    last = i
        z = z_table(l)
        i = m + 1
        while i < len(l):
            if last and i > last:
                last = None
            if (j := i + m - 1) in wild:
                last = j
            if (start := i - (m + 1)) < n and str1[i - (m + 1)] == 'F' and z[i] == m:
                if not last:
                    return ''
                l[last] = 'b'
                i = j + 1
            else:
                i += 1
        return ''.join(l[m + 1:])
