class Solution:
    def countNumbers(self, n):
        # code here
        limit = int(n ** 0.5) + 1

        # Sieve primes up to sqrt(n)
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        primes = []

        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        count = 0

        # Count numbers of form p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        # Count numbers of form p^2 * q^2
        for i in range(len(primes)):
            p_sq = primes[i] ** 2
            if p_sq > n:
                break
            for j in range(i + 1, len(primes)):
                q_sq = primes[j] ** 2
                if p_sq * q_sq > n:
                    break
                count += 1

        return count
