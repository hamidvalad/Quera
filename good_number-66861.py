#https://quera.ir/problemset/university/66861/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AF%D8%A7%D9%86%D8%B4%DA%AF%D8%A7%D9%87-%D8%B5%D9%86%D8%B9%D8%AA%DB%8C-%D8%B4%D8%B1%DB%8C%D9%81-%D9%85%D8%A8%D8%A7%D9%86%DB%8C-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87%D9%86%D9%88%DB%8C%D8%B3%DB%8C-%D9%BE%D8%A7%DB%8C%DB%8C%D8%B2-%DB%B9%DB%B8-%D8%B9%D8%AF%D8%AF-%D8%AE%D9%88%D8%A8

k = int(input())

i = 1
num = 0

while True:
    num += i
    i += 1
    count = 1
    for d in range(1, num):
        if num % d == 0:
            count += 1
    if count >= k:
        print(num)
        break