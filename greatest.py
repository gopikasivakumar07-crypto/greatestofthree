def greatest(a, b, c):
    return max(a, b, c)


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))

    print("Greatest number:", greatest(a, b, c))