pattern = int(input("Enter the size of the pattern:"))
row = 0
while row < pattern:
    for i in range(0, pattern):
        print("*", i, end="")
    print()
    row += 1
