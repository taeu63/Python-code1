
#성적 평균 구하기 성적 입력 후 평균 출력
recs=[]
for i in range(1,4):
  rec=int(input("성적을 입력하세요:"))
  recs.append(rec)
aver=sum(recs)/len(recs)
print("성적평균은 %d 입니다" %aver)
 
overaver=[]
for a in recs:
  if a>=aver:
    overaver.append(a)
print("%d점 이상인 학생은"%aver, len(overaver),"입니다")



#구구단 2~9단 입력 후 출력
if __name__ == "__main__": 

    num = int(input("2-9 사이의 단을 입력하세요 : "))

    while (num < 2 or num > 9):

        print("잘못 입력되었습니다")
        num = int(input("2-9 사이의 단을 다시 입력하세요 : "))

    for i in range(1, 10):
        print(num, "x", i, "=", num * i)