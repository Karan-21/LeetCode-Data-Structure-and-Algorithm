def m(x: int) -> int:
    return x if x > 0 else 0


def min_length_needed(remaining_primes: dict[int, int]) -> int:
    # I take as many 9s as I can
    result = m(remaining_primes[3]) // 2
    # I take as many 8s as I can
    result += m(remaining_primes[2]) // 3
    # I take as many 7s as I can
    result += m(remaining_primes[7])
    # I take as many 6s as I can
    result += min(m(remaining_primes[2]) % 3, m(remaining_primes[3]) % 2)
    # I take as many 5s as I can
    result += m(remaining_primes[5])
    # I take as many 4s as I can
    result += (
        m(remaining_primes[2]) % 3 - min(m(remaining_primes[2]) % 3, m(remaining_primes[3]) % 2)
    ) // 2
    # I take as many 3s as I can
    result += (
        m(remaining_primes[3]) % 2 - min(m(remaining_primes[2]) % 3, m(remaining_primes[3]) % 2)
    )
    # I take as many 2s as I can
    result += (
            m(remaining_primes[2]) % 3 - min(m(remaining_primes[2]) % 3, m(remaining_primes[3]) % 2)
    ) % 2

    return result


assert min_length_needed({2: 0, 3: 0, 5: 0, 7: 0}) == 0
assert min_length_needed({2: 1, 3: 1, 5: 1, 7: 1}) == 3
assert min_length_needed({2: 0, 3: 1, 5: 1, 7: 1}) == 3
assert min_length_needed({2: 3, 3: 0, 5: 0, 7: 0}) == 1
assert min_length_needed({2: 3, 3: 2, 5: 0, 7: 0}) == 2


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        ## Find the "kind of prime factorisation" of t (log(t))
        t_copy: int = t
        t_kinda_primes: dict[int, int] = defaultdict(int)
        for i in range(9, 1, -1):
            while t_copy % i == 0:
                t_kinda_primes[i] += 1
                t_copy //= i
        if t_copy != 1:
            # it means t is divisible by a prime number greater than 11
            return "-1"

        ## Find the optimal string if we didn't care about num (O(n))
        optimal_string: str = (
            "1" * (len(num) - sum(t_kinda_primes.values())) +
            "2" * t_kinda_primes[2] +
            "3" * t_kinda_primes[3] +
            "4" * t_kinda_primes[4] +
            "5" * t_kinda_primes[5] +
            "6" * t_kinda_primes[6] +
            "7" * t_kinda_primes[7] +
            "8" * t_kinda_primes[8] +
            "9" * t_kinda_primes[9]
        )
        if len(optimal_string) > len(num) or optimal_string > num:
            # - if len(optimal_string) > len(num) it means that we are in a scenario where maybe t 7*7*7 and num = 1
            # - the second if statement is optimal_string > num and that means len(optimal_string) == len(num) and
            # if optimal_string > num then optimal_string is the answer because optimal_string is the smallest
            # number we can get such that multiplying all its digits get us t
            return optimal_string

        ## Get rid of the 0s in num (O(n))
        num_l: list[int] = [int(d) for d in num]
        n: len(num_l) = len(num_l)
        for i in range(n):
            if num_l[i] == 0:
                # 509 -> 511
                for j in range(i, n):
                    num_l[j] = 1
                break

        ## Get product of integers in num mod t (O(n))
        product: int = 1
        for i in range(n):
            product *= num_l[i]
            product %= t
            if product == 0:
                return "".join(map(str, num_l))

        ## Brute-forcing won't work if done incorrectly
        # num = 6777277777 and t = 2*7**9 => the answer is obviously 7777277777

        # Claim: I can ignore up to the first n - sum(t_kinda_primes.values()) - 1 digits of num
        # num = 164523156151121321231111, t = 7*7*7 => 164523156151121321231777 works
        # num = 164523156151121321231888, t = 7*7*7 => 164523156151121321231777 doesn't work but
        #                                              164523156151121321232777
        # num = 0999999999999999999999888, t = 7*7*7 => 1111111111111111111111777 works
        #                                               this is just "1" + optimal_string

        ## Let's find this "shortest suffix" I can look at (O(n))
        num_l.insert(0, 0)  # O(n)
        n = len(num_l)
        mid: int = -1  # when do I start caring about changing the digits
        for i in range(n - sum(t_kinda_primes.values()) - 1, -1, -1):
            if num_l[i] != 9:
                mid = i
                break
        if mid == -1:
            return "1" + optimal_string

        ## From now on we only have to care about num_l[mid:]
        t_copy: int = t
        t_primes: dict[int, int] = defaultdict(int)
        for i in [2, 3, 5, 7]:
            while t_copy % i == 0:
                t_primes[i] += 1
                t_copy //= i

        product_up_to_mid: int = 1
        remaining_primes: dict[int, int] = t_primes.copy()
        for i in range(1, mid):
            product_up_to_mid *= num_l[i]
            product_up_to_mid %= t
            if num_l[i] in [2, 3, 5, 7]:
                remaining_primes[num_l[i]] = max(0, remaining_primes[num_l[i]] - 1)
            elif num_l[i] == 4:
                remaining_primes[2] = max(0, remaining_primes[2] - 2)
            elif num_l[i] == 6:
                remaining_primes[2] = max(0, remaining_primes[2] - 1)
                remaining_primes[3] = max(0, remaining_primes[3] - 1)
            elif num_l[i] == 8:
                remaining_primes[2] = max(0, remaining_primes[2] - 3)
            elif num_l[i] == 9:
                remaining_primes[3] = max(0, remaining_primes[3] - 2)

        ## I know what primes I need to "add" to get t. I know which part of num I can ignore.
        ## And so maybe the brute force will be more legitimate.

        def dfs(idx: int, free: bool) -> bool:
            ## if returns True, I found a number bigger than num the digits of which multiply to t
            if min_length_needed(remaining_primes) > n - idx:
                return False
            nonlocal product_up_to_mid
            if idx == n:
                return product_up_to_mid == 0
            for digit in range(1 if idx != 0 else 0, 10):
                if not free and digit < num_l[idx]:
                    # invalid change (for example num = 097 and idx = 2 and digit = 6)
                    continue

                # update remaining_primes
                if digit in [2, 3, 5, 7]:
                    remaining_primes[digit] -= 1
                elif digit == 4:
                    remaining_primes[2] -= 2
                elif digit == 6:
                    remaining_primes[2] -= 1
                    remaining_primes[3] -= 1
                elif digit == 8:
                    remaining_primes[2] -= 3
                elif digit == 9:
                    remaining_primes[3] -= 2

                old_num_l_idx: int = num_l[idx]
                old_product_up_to_mid: int = product_up_to_mid
                num_l[idx] = digit
                product_up_to_mid = (product_up_to_mid * digit) % t if digit != 0 else product_up_to_mid

                if dfs(idx + 1, free or digit > old_num_l_idx):
                    return True

                product_up_to_mid = old_product_up_to_mid
                num_l[idx] = old_num_l_idx

                # update remaining_primes
                if digit in [2, 3, 5, 7]:
                    remaining_primes[digit] += 1
                elif digit == 4:
                    remaining_primes[2] += 2
                elif digit == 6:
                    remaining_primes[2] += 1
                    remaining_primes[3] += 1
                elif digit == 8:
                    remaining_primes[2] += 3
                elif digit == 9:
                    remaining_primes[3] += 2
            return False

        dfs(mid, False)

        if num_l[0] == 0:
            # 097 -> 098
            return "".join(str(ch) for ch in num_l[1:])
        # 097 -> 115
        return "".join(str(ch) for ch in num_l)


if __name__ == "__main__":
    solution: Solution = Solution()

    assert solution.smallestNumber(num = "11111", t = 26) == "-1"
    assert solution.smallestNumber(num = "1", t = 8) == "8"
    assert solution.smallestNumber(num = "1234", t = 256) == "1488"
    # 256 = 4*8*8 so optimal_string is 488 but the answer cannot be 488 because 488 < 1234
    # so maybe I could just add a 1 at the beginning and then 1488 > 1234
    assert solution.smallestNumber(num = "12355", t = 50) == "12355"

    assert solution.smallestNumber(num = "164523156151121321231111", t = 7*7*7) == "164523156151121321231777"
    assert solution.smallestNumber(num = "6777277777", t = 2*7**9) == "6777777777"
    assert solution.smallestNumber(num = "4321", t = 256) == "4388"
    assert solution.smallestNumber(num = "50", t = 1) == "51"
    assert solution.smallestNumber(num = "50", t = 2) == "52"
    assert solution.smallestNumber(num = "50", t = 5) == "51"
