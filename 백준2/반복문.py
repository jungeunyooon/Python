# 2739

# n = int(input())
# for i in range(1,10):
#     print(n,"*",i,"=",n*i)

# 10950

# t = int(input())
# for i in range(1,t+1):
#     a,b = map(int,input().split())
#     print(a+b)

# 8393

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

# 25304

# x = int(input())
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     a,b = map(int,input().split())
#     sum += a*b
# if sum == x :
#     print("Yes")
# else : print("No")

# 15552

# import sys

# t = int(sys.stdin.readline())

# for i in range(1,t+1):
#     a,b=map(int,input().split())
#     print(a+b)

# 2438

# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)

# 2439

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)