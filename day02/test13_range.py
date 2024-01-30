# date : 2024-01-30
# file : test13_range.py
# desc : 리스트 범위지정

list_a = [1,2,3,4,5,6,7,8,9,10]

print(list_a)

# 범위 지정 range(n), 0부터 n개의 범위 수를 생성
print(range(5)) # range만 쓰면 안나옴
print(list(range(5)))
print(list(range(1, 6))) # 1~5
print(list(range(2, 21, 2))) # 2부터 20(+1)까지 2씩 증가하면서
print(list(range(1, 20, 2))) # 1부터 19(+1)까지 2씩 증가
print(list(range(10, -1, -1))) # 카운트다운 가능     # 10부터 0까지 -1씩 감소

list_a = list(range(1, 101))  # range() 클래스
print(list_a)

list_a = [i for i in range(1, 101)] # 리스트 컨프리핸션
print(list_a)