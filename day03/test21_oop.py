# date : 2024-01-31
# file : test21_oop.py
# desc : 객체지향 클래스 만들기
# CTRL + /는 전체 # 처리
# Ex) 붕어빵 틀 = 클래스, 붕어빵 = 객체
# 객체를 나타내는 명사는 변수, 행동은 함수
# class 클래스명:

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person: # 사람 클래스 선언
    name = '' # 멤버변수
    age = 0 # 멤버변수
    gender = '' # 클래스 안에 들어가는 변수 = 멤버변수

    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할 때 동작, 클래스에서 부르면 자동으로 튀어나옴
    # init == initialization(초기화)
    def __init__(self) -> None: # init 생성자는 return이 없음 알아서 보냄
        self.name = '홍길동'
        self.age = 99
        self.gender = '남자'

    # 클래스를 호출할 때 원하는 형태로 변환해서 보여줄 때 이 함수를 사용
    def __str__(self) -> str: # str 생성자(스페셜)는 return이 필요
        strs = f'커스텀 출력, 이름 {self.name} 객체 생성!'
        return strs

    def walk(self): # 멤버함수   매개변수 self는 필수
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')
# 사람 객체 생성, Instance(사례, 예제)
gd = Person() # 함수호출처럼 작성하면 됨
hd = Person()

# print(type(gd))
# print(id(gd)) # 다른 객체인지 확인할 때
# print(id(ac))
 
gd.name = '고길동' # 객체명.멤버변수 = ...
gd.age = 43
gd.gender = '남자'

hd.name = '고희동'
hd.age = 3
hd.gender = '남자'

print(f'gd => 이름:{gd.name} / 나이:{gd.age}세 / 성별:{gd.gender}')
print(f'hd => 이름:{hd.name} / 나이:{hd.age}세 / 성별:{hd.gender}')

gd.walk()
print('1분동안 걷는다')
gd.stop()

hd.walk()
print('걷기 싫어함')
hd.stop()


print('생성자 함수 추가-------------------------------------')
gg = Person()
print(f'gg => 이름:{gg.name} / 나이:{gg.age}세 / 성별:{gg.gender}')
print(gg)

