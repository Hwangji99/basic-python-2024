# date : 2024-01-31
# file : test20_funtion.py
# desc : 함수 만들기 (계산기 기능)
# def 함수명 (매개변수):
    # 쓸꺼
    # 쓸꺼

def add(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result

def multi(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y
    return result

def say_hello() -> None: # None은 의미를 부여할 수 없는 값, 값없는 값
    print('Hello')
    # return None은 쓸 필요가 없기 때문에 생략

say_hello()
print('더하기 - > ')
a, b = map(int, input('두 정수 입력 -> ').split(' '))
결과 = add(a, b) # 리턴은 함수 결과값으로 바뀐다
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a, b)}')
print(f'{a} X {b} = {multi(a, b)}')
print(f'{a} ÷ {b} = {divide(a, b)}')


