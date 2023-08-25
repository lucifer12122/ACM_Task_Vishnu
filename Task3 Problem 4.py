def fibonacci_sequence(n):
    x = [1, 2]
    while len(x) < n:
        x.append(x[-1] + x[-2])
    return x

def main():
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        N = int(input())
        sequence = fibonacci_sequence(N)
        print(sequence)

if __name__ == "__main__":
    main()
