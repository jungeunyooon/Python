# for i in range(1,51):
#     if i%2 == 0:
#         print(i,end=" ")

# myList = [ 11,22,23,99,81,93,35]
# sum = 0
# for i in myList:
#     sum = i + sum
#     print(sum)

# sum = 0 
# for i in range(1,101):
#     if i%3==0:
#         sum = i + sum
# print(sum)

# x = int(input("정수를 입력하시오 :"))
# for i in range(1,x+1):
#     if x%i==0 :
#         print(i,end=" , ")

# i = int(input("정수를 입력하시오 : "))
# for i in range(1,i+1):
#     print("\n")
#     for j in range(1,i+1):
#         print(j,end=" ")

# 5장

# def get_peri(radius=5.0):
#     area = 3.14*radius*radius
#     print(area)
# get_peri()
# get_peri(4.0)

# 6장

# n = int(input("입력할 값의 개수 : "))
# myList=[]
# for i in range(n):
#     value = int(input(" "))
#     myList.append(value)
# x = sum(myList)
# print(x)
 

# 2번 맞지만 리스트를 활용하지 않았다.

# import random

# for i in range(1,11):
#     x = random.randint(1,100)
#     print(x,end="  ")

# import random 
# list = []
# for i in range(10):
#     list.append(random.randint(1,100))
# print(list)

# 3번

# numbers = [20,1,12,9,18]
# for value in numbers:
#     print(value,"\t","*"*value)

## 7장

# 1번

# mylist = [80,20,20,30,60,30]
# print("주어진 리스트 :",mylist)
# myList =list(set(mylist))
# print("정리된 리스트 :",myList)

# 2번
# dic = { x:x**2 for x in range(1,11)}
# print(dic)

# 3번

# d = {"APPLE":1,"BANANA":2,"GRAPE":3}
# for k,v in d.items():
#     print(k,"->",v,)

# 4번

# d = {1:10,2:20,3:30,4:40,5:50,6:60}
# k = int(input("키를 입력하시오 :"))
# if k in d:
#     print("키",k,"은 딕셔너리에 있습니다.")
# else:
#     print("없습니다")

# 6번

# colors = ["red","green","blue"]
# values = ["#FF0000","#008000","#000FF"]
# dic = dict(zip(colors,values))
# print(dic)

# 8번
 
# d = {1:"january",2:"feburary",3:"march",4:"april",5:"may",6:"june",7:"july",8:"august",9:"september",10:"october",11:"november",12:"december"}
# x = int(input("달의 번호 :"))
# if x in d:
#     value = d[x]
# print("달의 이름 : ",value)

# 9번

# s1 = input("첫번째 문자열 :")
# s2 = input("두번째 문자열 :")
# s1 = set(s1)
# s2 = set(s2)
# list = list(set(s1)&set(s2))
# print("모두 포함된 글자 : ",list,end=" , ")

# 13번

# def count_all(txt):
#   return {
#     "LETTERS": sum(1 for x in txt if x.isalpha()),
#     "DIGITS": sum(1 for x in txt if x.isnumeric()),
#   }
# print(count_all("Hello World123"))