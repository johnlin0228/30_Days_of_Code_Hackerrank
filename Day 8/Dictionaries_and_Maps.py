n = int(input())

phone_book = {}

for i in range(0, n):
    input_arr = input().split(" ")
    name = input_arr[0]
    phone_num = input_arr[1]
    phone_book[name] = phone_num

for j in range(0, n):
    query_name = input()
    if query_name in phone_book:
        match_phone_num = phone_book[query_name]
        print(query_name + "=" + match_phone_num)
    else:
        print("Not found")
