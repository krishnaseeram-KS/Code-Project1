def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes(count):
    """Generate the first 'count' prime numbers."""
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


if __name__ == "__main__":
    # Generate the first 50 prime numbers
    primes = generate_primes(50)
    
    print(f"The first 50 prime numbers are:\n")
    for i, prime in enumerate(primes, 1):
        print(f"{i:2d}. {prime}")
    
    print(f"\nTotal: {len(primes)} primes")