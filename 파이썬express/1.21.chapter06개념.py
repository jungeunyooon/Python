# 5장 프로그래밍

# 10번

# def testPrime(n):
#     n >2 and n < 100
#     for i in range(2,n+1):
#         if n%i != 0 :
#             return True
#         print(i,end=" ")

# 틀렸음 다시해
            


# 11번

# def deci2bin(n):
#     binary = ""

#     while n != 0 :
#         value = n % 2
#         if value == 0 :
#             binary = "0" + binary
#         else :
#             binary = "1" + binary
#         n = n//2

#     return binary

# x = int(input("10진수 :"))
# print(deci2bin(x))

# 12번

#     n = x,y
#     return print(n)

# n1 = int(input("첫번째 정수 :"))
# n2 = int(input("두번째 정수 :"))
# getSorted(n1,n2)

# def getSorted(x,y): 
#     List = []
#     if x > y :
#         List = [ y,x ]
#         return List
#     else :
#         List[x,y]
#         return List
# x = int(input("첫 번째 정수 : "))
# y = int(input("두 번째 정수 : "))

# print(getSorted(x,y))


# 6장. 리스트

# temps = [28,31,33,35,27,26,25] # 초기값을 가진 리스트 생성
# e = temps[3] # 리스트의 요소에 접근

# temps = [28,31,33,35,27,26,25]
# for i in range(len(temps)):
#     print(temps[i],end="  ")

# temps = [28,31,33,35,27,26,25]
# for element in temps:
#     print(element,end="")

# questions = ["name","quest","color"]
# answers = ["kim","파이썬","blue"]
# for q,a in zip(questions,answers):
#     print(f"what is your {q} It is {a}")

# import random

# numberList = [1,2,3,4,5,6,7,8,9,10]
# print("랜덤하게 선택한 항목 = ",random.choice(numberList))

# STUDENTS = 5
# List = [] # 공백 리스트 생성
# count = 0

# for i in range(STUDENTS):
#     value = int(input("성적을 입력하시요 :"))
#     List.append(value)

# print("\n성적평균 = ",sum(List)/len(List))
# print("최대점수=",max(List))
# print("최소점수=",min(List))

# for score in List:
#     if score >= 80 :
#         count += 1
# print("80점 이상 =",count)

# list1 = [1,2,3,4,15,99]

# list.sort() # 리스트 정렬
# print("두번째로 큰수 =",list1[-2])

# list1 = [1,2,3,4,15,99]
# list1.remove(max(list1))
# print("두번째로 큰수=",max(list1))

# 친구 관리 프로그램

# menu = 0
# friends = []
# while menu != 9 :
#     print("-----------------")
#     print("1.친구 리스트 출력")
#     print("2.친구추가")
#     print("3.친구삭제")
#     print("4.이름변경")
#     print("9.종료")
#     menu = int(input("메뉴를 선택하시오:"))
#     if menu == 1 :
#         print(friends)
#     elif menu == 2 :
#         name = input("이름을 입력하시오:")
#         friends.append(name)
#     elif menu == 3 :
#         del_name = intput("삭제하고 싶은 이름을 입력하시오 :")
#         if del_name in friends:
#             friends.remove(del_name)
#         else :
#             print("이름이 발견되지 않았음")
#     elif menu == 4 :
#         old_name = input("변경하고 싶은 이름을 입력하시오 :")
#         index = friends.index(old_name)
#         new_name = input("새로운 이름을 입력하시오 :")
#         friends[index] = new_name
#     else :
#         print("이름이 발견되지 않았음")

# # 얕은 복사
# temps = [28,31,33,35,27,26,25]
# values = temps
# # 깊은 복사
# temps = [28,31,33,35,27,26,25]
# values = list(temps)

# import time
# SIZE = 50000

# start_time = time.time()
# mylist=[]
# for i in range(SIZE):
#     mylist = mylist + [i*i]
# print("수행시간=",time.time()-start_time)

# start_time = time.time()
# mylist = []
# for i in range(SIZE):
#     mylist.append(i*i)
# print("수행시간=",time.time()-start_time)

# numbers = [10,20,30,40,50,60,70,80,90]
# numbers[:3] # [10,20,30]
# numbers[3:] # [40,50,60,70,80,90]
# numbers[:] # [10,20,30,40,50,60,70,80,90]
# new_numbers = numbers[:] # 리스트의 복사본 생성

# list = [1,2,3,4,5,6,7,8]
# list[0:3] = ["w","b","r"] # ["w","b","r",4,5,6,7,8 ]
# list[::2] = [99,99,99,99] # [ 99,2,99,4,99,6,99,8]
# list[:] = [] # []

# s = "Monty Python"
# print(s[0])
# print(s[6:10])
# print(s[-12:-7])
# # 공백도 리스트에 포함

# def func1():
#     x = 42
#     print("x=",x,"id=",id(x))

# y = 10
# func1(y)
# print("y=",y,"id=",id(y))

# def func2(list):
#     list[0] = 99
# values = [ 0,1,1,2,3,5,8]
# func2(values)
# print(values) # [99,1,1,2,3,5,8]

# rows = 3
# cols = 5
# s = []
# for row in range(rows):
#     s += [ [0]*cols ]
# print("s=",s)

# s = [ [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]]

# rows = len(s)
# cols = len(s[0])

# for r in range(rows):
#     for c in range(cols):
#         print(s[r][c],end="")
#     print()








