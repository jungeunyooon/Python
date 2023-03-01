# 6장 프로그래밍

# 1번

# n = int(input("입력할 값의 개수 :"))
# list1 = []

# for i in range(n):
#     value = int(input(" "))
#     list1.append(value)
# x = sum(list1)
# print("값의 합계 =",x)

# 2번

# import random

# list= []

# for i in range(10):
#     list.append(random.randint(1,100))

# print(list)

# 3번

# numbers = [20,1,12,9,18]

# for value in numbers :
#     print(value,"\t","*"*value)

# 4번 

# list = [1,2,3,4,5,6,7,8,9,10]
# list = [-x for x in list if 3<=x<=8]
# print([1,2]+list+[9,10])

# 5번

# def match_words(words):
#     ctr=0

#     for word in words:
#         if len(word)>1 and word[0] == word[-1]:
#             ctr +=1
#     return ctr
# s = ["aba","xyz","abc","121"]
# print(s)
# print("문자열의 개수 =",match_words(s))

# 6번


# list1 = list(map(int,input("리스트1을 입력하시오 : ").split()))
# list2 = list(map(int,input("리스트2을 입력하시오 : ").split()))
# # split : 입력값이 여러개일 때, 띄어쓰기로 원소를 하나하나 나눠주는거
# # map : 리스트의 요소를 지정된 함수로 처리해주는 함수
# def com(m,n):
#     for m_o in m:
#         for n_o in n:
#             if m_o == n_o:
#                 result = True
#             else :
#                 result = False
#     return result

# print(list1)
# print(list2)
# com(list1,list2)
# print(com(list1,list2))

# 7번 

# import random
# list1 = ["a0","a1","a2","a3","a4","a5","a6","a7","a8","a9"]
# print("list1=",list1)
# print(random.choice(list1))

# 8번

a = [1,2,3,4,5]
b = [1,3,3,4,5,6,7]

c = [ x for x in a if x in b ]
print("a=",a)
print("b=",b)
print("결과=",c)

