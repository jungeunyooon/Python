# a = int(input("첫번째 정수를 입력하시오 :"))
# b = int(input("두번째 정수를 입력하시오 :"))
# if -10000 <= a <= 10000 and -10000 <= b <= 10000 :
#     if a>b :
#         print(">")
#     elif a<b:
#         print("<")
#     elif a==b:
#         print("==")
# else :
#     print("제한을 벗어남")


# a=1
# b=2

# if a>b :
#     print(">")
# elif a<b:
#     print("<")
# elif a==b:
#     print("==")


# print("Hello World!")

# a, b = map(int, input().split())
# print(a+b)


# a,b = map(int,input().split())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# id = input()
# print(id+"??!")
# # print(input()+"??!") 한줄 요약 가능

# y = int(input("불기 연도:"))
# z = y - 543
# print("서기 연도 : ",z)

# k,q,l,b,n,p = map(int,input().split())
# k1 = 1 
# q1 = 1
# l1 = 2
# b1 = 2
# n1 = 2
# p1 = 8
# print(k1-k,q1-q,l1-l,b1-b,n1-n,p1-p)

# origin = [1,1,2,2,2,8]
# cur = list(map(int,input().split()))
# for i in range(6):
#     print(origin[i]-cur[i],end=" ")


# a,b = map(int,input().split())
# if a > b :
#     print(">")
# elif a < b :
#     print("<")
# elif a==b : 
#     print("==")
# # 간단하게 한 줄 요약 가능
# print('>') if a > b else print('<') if a < b else print('==')

# score = int(input("시험 점수 : "))
# if score < 0 or score > 100 :
#     print("잘못된 점수")
# elif 90 <= score <= 100 :
#     print("A")
# elif 80 <= score <= 89 :
#     print("B")
# elif 70 <= score <= 79 :
#     print("C")
# elif 60 <= score <= 69 :
#     print("D")
# else :
#     print("F")

# year = int(input("연도 : "))
# if (year%4 == 0 and year%100!=0) or year%400==0:
#     print("1")
# else :
#     print("0")

# x,y = map(int,input().split())
# if x>0 and y >0 :
#     print("1") #Quadrant1
# elif x<0 and y>0 :
#     print("2") #Quadrant2
# elif x<0 and y<0 :
#     print("3") #Quadrant3
# elif x>0 and y<0 :
#     print("4") #Quadrant4

## 2884
# h,m = map(int,input().split())
# m1 = m-45
# if m1 < 0 :
#     m1 = 60+m1
#     if h > 0 :
#         h = h-1
#     else :
#         h = 23
#     print(h,m1)
# else :
#     print(h,m1)

## 2525

# a,b = map(int,input().split())
# c = int(input())
# a = ((b+c)//60) + a
# if b+c >= 60 :
#     b = (b+c)%60    
#     if a >= 24 :
#         a -= 24
#     print(a,b)
# else :
#     if a >= 24 :
#         a -= 24
#     print(a,b+c)

# 2480

a,b,c = map(int,input().split())
money = 0
if a==b==c :
    money = 10000+(a)*1000
    print(money)
elif a==b or a==c or b==c :
    if a==b or a==c :
        money = 1000+(a)*100
    else :
        money = 1000+(c)*100
    print(money)
else :
    money = max(a,b,c)*100
    print(money)


    

