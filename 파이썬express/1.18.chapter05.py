# print("안녕하세요?")
# print("철수님의 생일을 축하드립니다.")

# print("안녕하세요?")
# print("영희님의 생일을 축하드립니다.")

# # 함수로 중복 제거

# def print_msg(name):
#     print("안녕하세요?")
#     print(name,"님의 생일을 축하드립니다.")

# print_msg("철수")
# print_msg("영희")


# 함수 형식

# def get_area(radius): # 함수 형성
#     area = 3.14*radius**2 # 명령문
#     return area # 값 반환

# result1 = get_area(3) # 인수 3
# result2 = get_area(20) # 인수 20

# print("반지름이 3인 원의 면적 :",result1)
# print("반지름이 20인 원의 면적 :",result2)

# def main():
#     print("20cm 피자 2개의 면적:",get_area(20)+get_area(20))
#     print("30cm피자 1개의 면적",get_area(30))

# def get_area(radius):
#     area = 3.14*radius**2
#     return area

# main()

# def sub(x,y,z):
#     print("x=",x,"y=",y,"z=",z)
# sub(10,20,30)
# # 위는 위치 인수 // 기본 인수 전달 방식
# sub(x=10,y=20,z=30)
# # 위의 식이 키워드 인수
# # x,y,z의 순서를 신경쓰지 않아도 된다. 
# # 하지만 위치 인수가 반드시 키워드 인수  
# # 앞에 나타나야 한다

# def varfunc(*args):
#     # *이 가변길이를 의미한다. 
#     print(args)

# print("하나의 값으로 호출")
# varfunc(10)
# print("여러개의 값으로 호출")
# varfunc(10,20,30)


# 주급 계산 프로그램

# def pay(rate,hour):
#     if hour > 30 :
#         money = rate*30 + 1.5*rate*(hour-30)
#     else : 
#         money = rate*hour
#     return money

# rate = int(input("시급을 입력하시오 : "))
# hour = int(input("근무 시간을 입력하시오 :"))
# print("주급은"+str(pay(rate,hour)))

# def get_info():
#     name = input("이름")
#     age = int(input("나이"))
#     return name, age

# st_name,st_age = get_info()
# print("이름은",st_name,"이고 나이는",st_age,"살입니다.")

# 프로그래밍 

# 1번

# def get_peri(radius=5.0):
#     peri = 2.0*3.14*radius
#     return peri

# print("get_peri()=",get_peri())
# print("get_peri(4.0)=",get_peri(4.0))

# 2번

# n1 = int(input("첫 번째 정수를 입력하시오 :"))
# n2 = int(input("두 번째 정수를 입력하시오 :"))

# def sum(n1,n2):
#     sum = n1 + n2
#     return print(sum)

# def minus(n1,n2):
#     minus = n1-n2
#     return print(minus)

# def mul(n1,n2):
#     mul = n1*n2
#     return print(mul)

# def div(n1,n2):
#     div = n1/n2
#     return print(div)

# sum(n1,n2)
# minus(n1,n2)
# mul(n1,n2)
# div(n1,n2)


# 3번

# n1 = int(input("첫 번째 정수를 입력하시오 :"))
# n2 = int(input("두 번째 정수를 입력하시오 :"))

# def calc(n1,n2) :
#     sum = n1 + n2
#     minus = n1-n2
#     mul = n1*n2
#     div = n1/n2
#     return print(sum,minus,mul,div,"이 반환되었습니다.")

# calc(n1,n2)


# 5번

# def checkPass(p):
#     digit,lower,upper = 0,0,0
#     if len(p) >= 8 :
#         for i in p :
#             if i.isupper():
#                 upper = 1
#             elif i.islower():
#                 lower = 1
#             elif i.isdigit():
#                 digit = 1
#         if upper and lower and digit :
#             print("사용할 수 있습니다.")
#         else :
#             print("사용할 수 없습니다. ")
#     else :
#         print("사용할 수 없습니다. 다시 입력하세요!")


# password = input("패스워드를 입력하시오 :")
# checkPass(password)


# def checkPass(p):
#     digit,lower,upper = 0,0,0
#     for i in p :
#         if i.isupper():
#             upper = 1
#         elif i.islower():
#             lower = 1
#         elif i.isdigit():
#             digit = 1
#     if upper and lower and digit :
#         print("사용할 수 있습니다.")
#     else :
#         print("사용할 수 없습니다. ")

# password = input("패스워드를 입력하시오 :")
# checkPass(password)

# 9번

# def number(a,b):
#     m = min(a,b)
#     for i in range(m,-1,1) :
#         if a%i == 0 and b%i == 0 :
#             print(i)
#             break
# x = int(input("첫번째 정수 :"))
# y = int(input("두번째 정수 :"))
# number(x,y)


# def getGCD(a, b):
#     gcd = 1 
#     i = 2   

#     while i <= a and i <= b:
#         if a % i == 0 and b % i == 0:
#             gcd = i 
#         i = i + 1

#     return gcd 

# x = int(input("첫 번째 정수: "))
# y = int(input("두 번째 정수: "))

# print(getGCD(x, y))


