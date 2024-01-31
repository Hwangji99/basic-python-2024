# date : 2024-01-31
# test19_starprint.py
# desc : 별 찍기 또는 피라미드 만들기
# 다른 언어로도 연습 필수

# *
# **
# ***
# ****
# *****
# 모르면 무조건 디버깅 하자  조사식에 i, j, range(1, 6), range(1, i + 1) 넣기

for  i in range(1, 6):
    # 첫번째 i가 1일 때는 rang(1, 2) 1번 반복
    # i가 2이면, range(1, 3) 2번 반복
    for j in range(1, i + 1):
        print('*', end='') # 엔터 대신 empty로 변환
    print() # 안쪽 for문이 끝나면 다음줄로

# 거꾸로
for  i in range(1, 6):
    # 첫번째 i가 1일 때는 rang(1, 6) 5번 반복
    # i가 2이면, range(1, 5) 4번 반복
    for j in range(1, 6 - i + 1):
        print('*', end='')

    print()

# 반대로 붙임
for  i in range(1, 6):
    
    for j in range(1, 6 - i + 1):
        print(' ', end='')

    for j in range(1, i + 1):
        print('*', end='')
    print()