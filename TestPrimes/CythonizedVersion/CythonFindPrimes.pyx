class CythonFindPrimes:
    def __init__(self, n):
        self.n = n

    def get_prime_numbers(self):
        p = []
        n = 2
        while len(p) < self.n:
            # Is n prime?
            for i in p:
                if n % i == 0:
                    break

            # If no break occurred in the loop
            else:
                p.append(n)
            n += 1
        return p
