# try:
#     f = open("test.txt","w")
#     f.write("홍길동")
# finally:
#     f.closer()

# with open("test.txt","w") as f:
#     f.write("김영희\n")
#     f.write("최자영\n")
# # 블록을 빠져나오면 자동으로 파일이 닫혀진다.

# infilename = input("입력 파일 이름 :");
# outfilename = input("출력 파일 이름 : ")

# infile = open(infilename,"r")
# outfile = open(outfilename,"w")

# sum = 0
# count = 0

# line = infile.reaaline()
# # readline은 한줄읽기
# while line!= "":
#     s = int(line)
#     sum += s
#     count += 1
#     line = infile.readline()

# outfile.write("총매출="+str(sum)+"\n")
# outfile.write("평균 일매출="+str(sum/count))

# infile.close()
# outfile.close()
