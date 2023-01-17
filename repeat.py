#요소 한줄씩 출력
a = [11, 22 ,33 ,44 ,55]
for i in a:
    print(i)

#같은 줄 다섯번 반복
a = [11, 22 ,33 ,44 ,55]
for i in range(5):
    print(a)

#인덱스를 함께 출력하는 방법1
i=0
a = [11, 22 ,33 ,44 ,55]
for m in a:
    print(i,m)
    i += 1

# 인덱스를 함께 출력하는 방법2
a = [11, 22 ,33 ,44 ,55]
for i in range(len(a)):
    number = a[i]
    print(number,i)

#for i in range(숫자) range는 연속된 숫자 생성,숫자를 하나씩 꺼내 i에 담음
for i in range(5):
    print(i)
#0부터 4까지 출력

#range증가 기본-양수1씩 증가
for i in range(0,10):
    print(i)
#range감소
for i in range(10,0,-1):
    print(i)

