Actual = input().split(" ")
Da = int(Actual[0])
Ma = int(Actual[1])
Ya = int(Actual[2])
Expected = input().split(" ")
De = int(Expected[0])
Me = int(Expected[1])
Ye = int(Expected[2])

fine = 0
if Ya < Ye:
    print(fine)
elif Ya == Ye:
    if Ma < Me:
        print(fine)
    elif Ma == Me:
        if Da <= De:
            print(fine)
        else:
            fine = (Da - De) * 15
            print(fine)
    else:
        fine = (Ma - Me) * 500
        print(fine)
else:
    fine = 10000
    print(fine)