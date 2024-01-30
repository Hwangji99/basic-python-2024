# date : 2024-01-30
# file : test14_while.py
# desc : while 문

## while 참인조건:
## 공통점 if 조건: elif 조건: else:, for in range():, while 조건:
count = 0

# while count < 10:  # count가 10보다 작은 동안 반복
# 무한루프 : Window OS, 모바일OS, 자동차 네비게이션, 라즈베리파이, 아두이노, 게임
#            Winform 개발, ....
while True: # 참인동안 True 항상 참 = 끝이 없음(무한 루프, Infinite Loop)
    count = count +1
    print('나무찍기 ', count)
    if count == 10:
        break # 이 반복문을 빠져나가라!

number = 0
while True:
    number = number + 1
    if str(number).count('3') >= 1 or \
        str(number).count('6') >= 1 or \
        str(number).count('9') >= 1: # 숫자를 문자열로 바꾼 값안에 '3', '6', '9'가 있으면
        print('짝!')
    else:
        print(number)

    if number == 30: break  # 반복문을 완전히 빠져나감

print('--------------------------------------------')
# 짝! 대신에 continue로 변경
# continue는 반복에서 제외
number = 0
while True:
    number = number + 1
    if str(number).count('3') >= 1 or \
        str(number).count('6') >= 1 or \
        str(number).count('9') >= 1: 
        continue # 3,6,9 들어가는 수를 반복에서 제외
    else:
        print(number)

    if number > 31: break
