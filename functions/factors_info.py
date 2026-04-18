num = int(input("Enter a number: "))

def factors_info(n):
    factor_sum = 0
    factor_count = 0
    
    print(f"Factors of {n}: ", end="")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
            factor_sum += i
            factor_count += 1
    
    print(f"\nSum of factors: {factor_sum}")
    print(f"Count of factors: {factor_count}")

factors_info(num)