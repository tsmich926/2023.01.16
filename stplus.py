print("hello"+"python")#헬로 파이썬 출력

print("hello"*3) #가로로 세번출력

#변수를 문자열에 넣는법
name="sua"
score=85
print(f'이름은 {name}고 점수는 {score}')

# f-string  < 사용해 왼쪽 정렬 [:<숫자] 숫자는 글자수
s1 = 'left'
result1 = f'|{s1:<10}|'
print(result1)
 
# f-string ^ 사용해 가운데 정렬
s2 = 'mid'
result2 = f'|{s2:^10}|'
print(result2)
 
# f-string > 사용해 오른쪽 정렬
s3 = 'right'
result3 = f'|{s3:>10}|'
print(result3)

# f-string 딕셔너리 사용
d = {'name': 'BlockDMask', 'gender': 'man', 'age': 100}
result = f'my name {d["name"]}, gender {d["gender"]}, age {d["age"]}'
print(result)

