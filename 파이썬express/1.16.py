# 2장 프로그래밍

# 1번

# x = int(input("x를 입력하시오 :"))
# y = int(input("y를 압력하시오 :"))

# print("x :", x)
# print("y :", y)
# print("두수의 합:",x+y)
# print("두수의 차 :",x-y)
# print("두수의 곱 :",x*y)
# print("두수의 평균 :",(x+y)/2)
# print("큰수 : ",max(x,y))
# print("작은 수 : ", min(x,y))

# 2번

# x = int(input("닭의 수 :"))
# y = int(input("돼지의 수 :"))
# z = int(input("소의 수 :"))
# print("전체 다리의 수 :",2*x+4*y+4*z)

# 3번

# x = int(input("삼각형의 첫 번째 변의 길이 :"))
# y = int(input("삼각형의 두 번째 변의 길이 :"))
# z = x+y-1
# print("삼각형의 나머지 변의 최대 길이 :", z)\

# 4번

# x = int(input("시간울 입력하시오 : "))
# y = int(input("분을 입력하시오 : "))
# z = x*3600+y*60
# print(x,"시간 ",y,"분은",z,"초입니다.")

# 5번

# f = int(input("화씨 온도를 입력하시오 : "))
# C = (f-32.0)*(5/9)
# print("화씨",f,"도는 섭씨",C,"도에 해당합니다.")

# 6번

# x = int(input("음식 비용 :"))
# print(" 팁 비율 : 10% ")
# y = x + int(x*0.1)
# print("총액 :", y,"달러")

# 7번

# x1 = float(input("x1="))
# y1 = float(input("y1="))
# x2 = float(input("x2="))
# y2 = float(input("y2="))
# distance = ((x1-x2)**2+(y1-y2)**2)**0.5
# print("두점 사이의 거리 =",distance)

# 9번

# number = int(input("정수 ="))
# x1 = number%10
# x2 = (number//10)%10
# x3 = (number//100)%10
# x4 = number//1000
# print(x1+x2+x3+x4)

# 12번

number = int(input("숫자를 입력하시오 :"))
a = number // 1000
b = number % 1000
print(a,",",b)
# 중요!! //은 정수 나눗셈 , % 나눗셈 연산자 

