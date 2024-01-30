# date : 2024-01-30
# desc : 흐름제어 (if문)

## 조건이 참일 때와 거짓일 때로 나누어서 어떤 일을 처리 = if
## 입력 input()로 받는 것은 문자
number = int(input('정수 입력 > ')) # 입력함수 int(input()) - 문자로 된 입력값을 정수로 변경

if number > 0:  # if 조건:    <- 참인 조건
    print('양수입니다.')
elif number == 0: # 양수X 음수X, 거짓인 조건    # elif = else if
    print('0입니다.')
elif number < 0:  # 거짓인 조건
    print('음수입니다.')
else:           # else:       <- 거짓인 조건  # 이 값은 나올 수 없기 때문에  이 줄은 빼도 된다
    print('정의할 수 없습니다.')



