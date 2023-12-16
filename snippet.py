# Python Code Snippet for Code Review

def calculate_fibonacci_sequence(n):
    """
    Calculate the Fibonacci sequence up to the n-th term.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        next_element = sequence[i-1] + sequence[i-2]
        sequence.append(next_element)

    return sequence

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_primes_in_fibonacci_sequence(sequence):
    """
    Filter out the prime numbers in a Fibonacci sequence.
    """
    return [num for num in sequence if is_prime(num)]

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
