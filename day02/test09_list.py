# date : 2024-01-30
# desc : 복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60 
# 총갯수 n이면 인덱스의 마지막 값은 n-1
# index =  0,   1,  2,  3,  4,  5,  6,  7, 8, 9
# index = -10, -9, -8, -7, -6, -5, -4, -3, -2, -1 
std = [80, 90, 100, 50, 60, 44, 66, 88, 99, 77]  # 학생수만큼 변수를 생성
# 리스트 요소에 접근
# 리스트는 대괄호([])를 쓴다
print(std[5])

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3, 4), std] # 파이썬 리스트에는 모든게 들어갈 수 있다
print(list_1)
print(list_1[5])

list_1[6] = '바꾼값' # 원래 리스트가 문자열로 변경
print(list_1)

## 리스트 연산
print(list_1[2:4]) # : 뒤의 수는 출력하고 싶은 인덱스 +1이 필수 (!), 파이썬만 이럼
## 마이너스 인덱스
print(list_1[-6:-3])
## 이중리스트
print(list_1[4][2]) # [1,2,3,4] 중 3만 가져오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2]) # 6

list_4 = [1,2,3]
list_5 = [7,8,9]
# list_3 = list_4 + list_5
## 리스트 연산 +, *만 사용가능 
print(list_4 + list_5) # +는 리스트를 연결할 때 사용
print(list_5 * 2) # *는 리스트를 반복할 때 사용

## 리스트 길이함수 len()
print(len(list_4))

## 리스트 추가 함수 append() 
# 리스트 마지막에 하나 추가

## 리스트 삽입 함수 insert()
# insert(index, val) 리스트의 index 앞에 val 추가
print(list_1)
list_1.append('Hello!!')

print(list_1)

list_1.insert(2, 100) # 2번째 인덱스에 값을 추가(원래 값은 뒤로 밀림)
print(list_1)

## 리스트 확장 함수 extend()
# +와 거의 유사
list_4.extend(list_5)
print(list_4)
print(list_5)

## 리스트 삭제 함수 del
del list_4[3]    # 리스트의 인덱스 하나를 삭제
print(list_4)
del list_4       # 리스트 자체를 삭제
# print(list_4)\

val = list_5.pop() # 마지막 값을 꺼내오기
print(val)         # 9
print(list_5)      # [7, 8]

print(std)
val = std.pop(2)  # 해당 위치에 인덱스를 꺼내옴
print(val)        # 100
print(std)        # [80, 90, 50, 60, 44, 66, 88, 99, 77]

# clear()
list_5.clear()    # del()은 완전 삭제 print도 안됨, clear()는 내용만 삭제
print(list_5)

# sort() # 문자열, 숫자, 불이 섞여있는 리스트는 정렬 안됨
std.sort() # 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not in     # 값이 리스트 안에(in) 있으면 True 아니면 False    not in은 결과를 반대로
print(99 in std) # True
print(55 in std) # False

# reverse(), copy(), count() ....
# *리스트 : 전개연산자 - 몰라도 됨
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)