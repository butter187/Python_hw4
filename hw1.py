# n = int(input("Введите 3-х значное число "))
# sum = 0
# while n > 0:
#     x = n % 10
#     sum = sum + x
#     n = n//10
# print(sum)   
# n = 123
# res = (n //10)%10
# print(res)

n=(input("Введите число шестизначное число "))
if int(n[0])+int(n[1])+int(n[2])==int(n[3])+int(n[4])+int(n[5]):
    print(f"{n} -> yes")
else:
    print(f"{n} -> no")