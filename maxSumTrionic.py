class Solution:
    def maxSumTrionic(self, A: List[int]) -> int:
        N = len(A)
        ans = -inf

        i = 0
        while i + 1 < N:
            if A[i] <= A[i + 1]:
                i += 1
                continue

            j = i
            while j + 1 < N and A[j] > A[j + 1]:
                j += 1
            if i == j:
                i += 1
                continue

            # A[i..j] is decreasing

            h = i
            s_left = 0
            m_left = -inf
            while h - 1 >= 0 and A[h-1] < A[h]:
                h -= 1
                s_left += A[h]
                m_left = max(m_left, s_left)

            k = j
            s_right = 0
            m_right = -inf
            while k + 1 < N and A[k] < A[k + 1]:
                k += 1
                s_right += A[k]
                m_right = max(m_right, s_right)

            if h < i < j < k:
                middle = sum(A[z] for z in range(i, j + 1))
                ans = max(ans, middle + m_left + m_right)

            i = j + 1

        return ans
