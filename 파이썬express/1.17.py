# 3장 조건문

# 배송비 계산 프로그램
# price = int(input("상품의 가격 : "))

# if price > 20000 : 
#     shipping_cost = 0
# else :
#     shipping_cost = 3000

# print("배송비 =",shipping_cost)

# price = int(input("상품의 가격 : "))

# shipping_cost = 3000
# if price > 20000 :
#     shipping_cost = 0

# price = int(input("상품의 가격 : "))

# if price > 20000 : 
#     pass
# else :
#     pass

# 부울변수

# radius = 100
# flag = (radius > 32) # flag에 저장
# print(flag)

# expensive = price > 20000
# if expensive :
#     shipping_cost = 0
# else :
#     shipping_cost = 3000
# print(expensive)

# 산술 문제 출제 프로그램

# import random

# x = random.randint(1,100) # 1,100사이의 난수 반환 
# y = random.randint(1,100) # 난수 : random number

# answer = int(input(f"{x}+{y}=")) # f-문자열사용
# flag = ( answer == (x+y) )
# print(flag)

# 짝수 홀수 검사 프로그램

# number = int(input("정수를 입력하시오 :"))

# if number%2 ==- 0 : # %는 나눗셈 출력 연산자
#     print("짝수입니다")
# else: 
#     print("홀수입니다.")

# 물의 상태 출력하기

# temp = int(input("온도를 입력하시오 :"))

# if temp <= 0 :
#     print("물의 상태는 얼음")
# elif temp < 100 and temp > 0 :
#     print("물의 상태는 액체")
# else :
#     print("물의 상태는 기체")

# 배송비 프로그램 

# country = input("배송지 : ")
# price = int(input("상품의 가격 : "))

# if country == 'korea':
#     if price >= 20000 :
#         shipping_cost = 0
#     else : 
#         shipping_cost = 3000

# else : 
#     if price >= 100000 :
#         shipping_cost = 0
#     else : 
#         shipping_cost = 8000
# print("배송비 =",shipping_cost)

# 학점 계산 프로그램

# score = int(input("점수를 입력하시오 : "))
# if score >= 60 :
#     print("학점 D")
# elif score >= 70 :
#     print("학점 C")
# elif score >= 80 :
#     print("학점 B")
# elif score >= 90 :
#     print("학점 A")
# else : 
#     print("학점 F")

# 프로그래밍 문제

# 1번

# n1 = int(input("정수를 입력하시오 : "))
# n2 = int(input("정수를 입력하시오 : "))

# if n1 % n2 == 0 :
#     print("약수입니다.")
# else : 
#     print("약수가 아닙니다.")

# 4번

# radius = float(input("원의 반지름 : "))

# if radius < 0 :
#     print("잘못된 값입니다.")
# else :
#     print("원의 면적 :",3.14*radius**2) 

# 5번

# x,y,z = eval(input("3개의 정수를 입력하시오 :"))
# # 3개의 정수를 동시에 입력받을 때 쓰는 명령문
# if x < y :
#     if x < z :
#         print("제일 작은 정수는",x,"입니다.")
#     else :
#         print("제일 작은 정수는",z,"입니다.")
# else :
#     if y < z :
#         print("제일 작은 정수는",y,"입니다.")
#     else :
#         print("제일 작은 정수는",z,"입니다.")

# 6번

# import random
 
# x = int(input("선택하시오(1: 가위 2: 바위 3: 보)"))
# y = random.randint(1,3)

# if x == 1 and y == 3 :
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("사용자가 이겼음")
# elif x == 1 and y == 2 :
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("컴퓨터가 이겼음")   
# elif x == 1 : 
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("비겼음")
# elif x == 2 and y == 3 :
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("컴퓨터가 이겼음")  
# elif x == 2 and y == 1 : 
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("사용자가 이겼음")
# elif x == 3 and y == 1 :
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("컴퓨터가 이겼음")  
# elif x == 3 and y == 2 : 
#     print("컴퓨터의 선택(1: 가위 2: 바위 3: 보)",y)
#     print("사용자가 이겼음")

# 9번

import random

number = int(input("숫자를 선택하시오 :"))
x = random.randint(1,10)
y = random.randint(1,10)
answer = 0

if number == 1 : # 덧셈
    answer = int(input(str(x)+"+"+str(y)+"의 값은?"))
    if answer == x+y :
        print("맞았습니다.")
    else :
        print("틀렸습니다.")
elif number == 2 : #뺄셈
    answer = int(input(str(x)+"-"+str(y)+"의 값은?"))
    if answer == x-y :
        print("맞았습니다.")
    else :
        print("틀렸습니다.")
elif number == 3 : #곱셈
    answer = int(input(str(x)+"*"+str(y)+"의 값은?"))
    if answer == x*y :
        print("맞았습니다.")
    else :
        print("틀렸습니다.")
elif number == 4 : #나눗셈
    answer = int(input(str(x)+"/"+str(y)+"의 값은?"))
    if answer == x/y :
        print("맞았습니다.")
    else :
        print("틀렸습니다.")
