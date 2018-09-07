N = int(input())

for i in range(0, N):
    str = input()
    evenStr = ""
    oddStr = ""
    for j in range(0, len(str)):
        if (j % 2 == 0):
            evenStr += str[j]
        else:
            oddStr += str[j]
    print(evenStr + " " + oddStr)
