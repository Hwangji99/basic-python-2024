# date : 2024-01-30
# desc : 홀수 / 짝수 구분 또는 배수

number = int(input('정수 입력 > ')) # 입력받은 후 정수로 변경

if number % 2 == 0: # 짝수 또는 배수
    print('짝수')
else:               # 홀수 또는 나머지
    pass            # print('홀수') # pass는 그냥 넘기는거임