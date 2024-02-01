# 파이썬 기초 2024
부경대 2024 It 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
   - 코딩 폰트 - 나눔고딕코딩
   - Notepad++ 설치
   - Python 설치
   - Visual studio Code 설치
   - Git 설치
       - TortoiseGit 설치
       - Github 가입
       - Github Desktop 설치

- 파이썬 기초
    - 파이썬 개발자는 귀도 반 로섬
    - 1990년대 귀도가 크리스마스 이브에 취미로 개발
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자
     
    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01))  # <class of 'int'>

    print(5 + 4 / 2) # 7.0
    print(5 == 4) # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참 / 거짓으로 조건 분기 (다른언어 switch)
            - 흐름제어 (if문)
            - 여러조건 if문
            - if문 응용
            - 홀수 / 짝수 구분 또는 배수
        - for : 반복문 기본 (다른언어 foreach)
        - while : 반복문 병형 (다른언어 do ~ while)
    - 복합자료형 + 연산자 (연산함수)
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷
    - 구구단 + 디버깅

```python
print('구구단 시작!')
for x in range(2, 10): # 2부터 9까지 반복
    print(f'{x}단 ------')
    for y in range(1, 10): # 1부터 9까지 반복
        print(f'{x} x {y} = {x*y:2d}', end = '  ') # end = 엔터 대신 공백으로 변경
    print() # 안쪽 for문이 끝나면 마직막 엔터를 하나 추가

# debugging 단축키
# F5(디버그 시작), F10(한줄씩 실행), F11(함수안으로 진입), F9(중단점 토글)
# Shift + F5(디버깅 종료)
# 조사식을 확인
```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별 찍기 (피라미드 만들기)
    - 함수, 람다함수(나중에)
    - 객체지향 (OOP)
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아 둔 곳 = 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화 (__platenumber)
    - 패키지

## 4일차
- 파이썬 기초
    - 패키지, 모듈 이어서
        - pip 사용

        ```shell
        > pip --version # 버전확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지를 삭제
        > pip install requests # request 패키지를 설치 Successfully가 뜨면 된 것
        ```
    - 예외처리 (중요) : 비정상적 프로그램 종료 막기

    ```python
    def divide(x, y):
        try:
            return x / y # ZeroDivisionError 발생\
        except ZeroDivisionError as e:
            print('[오류!!] 제수는 0일 될 수 없습니다.')
            return 0 # 아무것도 입력안하면 return None이 숨어있음
    ```
    - 텍스트 파일 입출력

    ```python
    f = open('파일명', mode='r│w│a', encoding='cp949│utf-8')
    f.read()
    f.readline() # 읽기
    f.write('text') # 쓰기
    f.close() # 파일은 반드시 닫는다
    ```
- 파이썬 활용
    - 주피터 노트북













    - 가상환경
    - 객체지향(나중)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중 상속
        - 추상클래스, 인터페이스


