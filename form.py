#format함수: 중괄호 {, } 안에 포매팅을 지정하고 format 함수의 인자로 값들 넣는다.
a=10
b=20
c=a*b
s='곱셈 출력 {0}x{1}={2}'.format(a,b,c)
print(s)

#직접 대입
s1 = '이름은 {0}'.format('수아')
print(s1)

#이름으로 대입
s2 = 'number:{num},gender={gen}'.format(num=123, gen='남')
print(s2)

