import math

def calculate_fibonacci_sequence(n):
    """
    Calculate the Fibonacci sequence up to the n-th term.
    """
    if n <= 0:
        return []
    sequence = [0, 1][:n]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes_in_fibonacci_sequence(sequence):
    """
    Filter out the prime numbers in a Fibonacci sequence.
    """
    prime_cache = {}
    return [num for num in sequence if num not in prime_cache and is_prime(num) and not prime_cache.setdefault(num, True)]

def main():
    """
    Main function to execute the program.
    """
    try:
        n = int(input("Enter the number of terms for Fibonacci sequence: "))
        if n <= 0:
            raise ValueError("Number of terms must be a positive integer.")

        fibonacci_sequence = calculate_fibonacci_sequence(n)
        print(f"Fibonacci Sequence (up to {n} terms): {fibonacci_sequence}")

        prime_numbers = filter_primes_in_fibonacci_sequence(fibonacci_sequence)
        print(f"Prime numbers in the Fibonacci sequence: {prime_numbers}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
