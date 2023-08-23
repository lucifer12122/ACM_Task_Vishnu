def main():
    inputs = int(input(" Number of inputs: "))
    numbers = [int(input(f"Enter number {i+1}: ")) for i in range(inputs)]
    total = sum(numbers)
    print(total)

main()
