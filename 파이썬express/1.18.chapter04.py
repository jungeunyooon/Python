# 4장 반복문

# 팩토리얼 계산하기

# n = int(input("정수를 입력하시오 :"))
# fact = 1
# for i in range(1,n+1) :
#     fact = fact*i
# print(n,"!은",fact,"이다.")

# 숫자 맞추기 게임

# import random

# tries = 0
# n2 = 0;
# n1 = random.randint(1,100)

# print("1부터 100까지의 숫자를 맞추시오")

# while n1 != n2 :
#     n2 = int(input("숫자를 입력하시오 :"))
#     tries = tries + 1
#     if n1 < n2 :
#         print("너무 높음!")
#     elif n1 > n2 :
#         print("너무 낮음!")

# if n1 == n2 :
#     print("축하합니다. 시도횟수=",tries)
# else :
#     print("정답은",n1)

# 중첩 반복문

# for y in range(1,6):
#     for x in range(y):
#         print("*",end="")
#     print(" ")
 
# 모든 조합 출력하기

# persons = ["kim","park","lee","choi"]
# restaurants = [ "koreans","american","french","chinese"]

# for person in persons :
#     for restaurant in restaurants :
#         print(person + "이" + restaurant + "식당을 방문")

# 소수 찾기 프로그램

# N_PRIMES = 50
# number = 2
# count = 0

# while count < N_PRIMES :
#     divisor = 2
#     prime = True

#     while divisor < number :
#         if number % divisor ==0 :
#             prime = False 
#             break;
#         divisor =+ 1
#     if prime :
#         count += 1
#         print(number,end=" ")
    
#     number += 1 

# 프로그래밍

# 1번

# for i in range(1,51):
#     if i%2 == 0 :
#         print(i,end="")

# 2번

# myList = [ 11,22,23,99,81,93,35 ]
# sum = 0
# for i in myList :
#     sum = sum + i
#     print(sum)

# 3번

# sum = 0

# for i in range(1,100):
#     if i%3 == 0 :
#         sum = sum + i
# print("1부터 100사이의 모든 3의 배수의 합은",sum,"입니다.")

# 4번

# number = int(input("정수를 입력하시오 :"))

# for i in range(1,number+1) :
#     if number%i == 0 :
#         print(i,end=",")

# 5번

# x = int(input("정수를 입력하시오 : "))

# for x in range(1,x+1):
#     for i in range(1,x+1):
#         print(i,end=" ")
#     print(" ")

# 8번

# n = 0 
# while n**2 <= 500 :
#     n = n+1 
# else : 
#     print(n)

# 9번

# for i in range(1,10):
#     for x in range(1,10):
#         x= i*x
#         print(x,end="  ")
#     print("  ")

# 11번

# x = int(input("첫 번째 정수를 입력하시오 :"))
# y = int(input("두 번째 정수를 입력하시오 :"))

# m = min(x,y)

# for m in range(1,m+1):
#     if x%m == 0 and y%m == 0 :
#         gcd = m 
# print("최대공약수=",gcd)


# 13번

# nterms = int(input("몇 번째 항까지 구할까요? "))

# n1, n2 = 0, 1
# count = 0

# while count <= nterms:
#        print(n1, end=" ")
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1


# 14번 

for i in range(2,21):
    result = True
    if i >= 2 :
        for j in range(2,i):
            if i%j == 0 :
                result = False
    if result :
        print(i,end=" ")
