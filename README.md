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
    ```python
    # 콘솔출력을 위해서는 print() 함수를 사용 (주석 : 소스 실행에 영향을 주지 않음)
    print('Hello, World!')

    # > python test01_console.py로 콘솔 실행
    # VS Code에서 Ctrl + F5 (실행 > 디버깅 없이 실행)
    ```
    - 주석
    - 변수
    ```python
    # 변수(Variable) - 변하는 수. 파이썬에서는 들어가는 종류나 크기에 제약이 없음(!)
    var01 = 10
    print(var01)

    var01 = False
    print(var01)

    var01 = 'Life is short, You need Python.'
    print(var01)

    # 단, 변수명을 지정시 아래는 불가
    ## - 숫자로 시작하거나
    ## - 공백이 있거나
    ## - _(언더바)이외의 특수문자가 있으면 안됨
    ```
    - 자료형
    ```python
    ## 기본자료형 - 숫자형, 문자형, 불형, None형
    ## 복합자료형 - 리스트형, 튜플형, 딕셔너리, 집합

    ## None형 == null (C, C++, C#, JAVA, SQL)
    ## 값은 값인데 아무것도 지정할 수 없는 값 => None
    apple = None
    print(apple)

    ## 숫자형 - 정수형, 실수형, 진수형
    ### 정수
    ten = 10
    hundred = 100
    temp = -8

    ### 실수
    pi = 3.141592
    test_val = 2e10
    print(test_val)

    ### 진수
    bit142 = 0b10001110 # 0 => 0, 1 => 1, 10 => 2, 11 => 3, 100 => 4, 101 => 5
                        # 110 => 6, 111 => 7, 1000 => 8 
    oct9 = 0o100        # 0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17,20,....,77,100
    hex255 = 0xFF       # 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
    print(bit142)
    print(oct9)
    print(hex255)

    ## 문자형 - 파이썬에는 문자, 문자열 차이가 없음
    greeting = 'Hello!'
    greeting = "Hello!" # 홑따옴표, 쌍따옴표 모두 문자열 나타냄
    print(greeting)

    ## 불형 (Bool, Boolean) - True or False
    isCheck = False
    print(isCheck)

    isCheck = True
    print(isCheck)

    ## 자료형이 어떤 타입인지 체크
    print(type(apple))
    print(type(test_val))
    print(type(greeting))
    print(type(isCheck))
    ```
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
            ```python
            ## 조건이 참일 때와 거짓일 때로 나누어서 어떤 일을 처리 = if
            ## 입력 input()로 받는 것은 문자
            number = int(input('정수 입력 > ')) # 입력함수 int(input()) - 문자로 된 입력값을 정수로 변경

            if number > 0:  # if 조건:    <- 참인 조건
                print('양수입니다.')
            elif number == 0: # 양수X 음수X, 거짓인 조건
                print('0입니다.')
            elif number < 0:  # 거짓인 조건
                print('음수입니다.')
            else:                
                print('정의할 수 없습니다.')
            ```
            - 여러조건 if문
            ```python
            date = input('날짜 입력 > ') #  문자열 입력

            month = date.split('-')[0] #  월
            day = date.split('-')[1] #  일

            if month == '12' and day == '25': # 12월 25일
                print('메리 크리스마스!!')
            elif month == '01' and day == '01': # 1월 1일
                print('해피 뉴이어~!!')
            else:
                print('보통날입니다')
            ```
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
        - Ctrl + Shift + P (명령 팔레트)로 시작
        - 사용방법 (test31_jupyternb.ipynb 참조)
    - 이미지 올리는 방법
        - 깃허브에 올린 이미지의 주소를 복사해 새 링크를 열어 붙임
        - 새로 나온 페이지 주소를 다시 복사
        - README.md에 ![이미지제목](복사한 주소)
    - folium 기본사용
    ![folium사용법](https://raw.githubusercontent.com/Hwangji99/basic-python-2024/main/images/python_001.png)

## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(Colab)
    - folium 이어서
    - JSON(JavaScript Object Notation) 입출력
    - 응용예제 연습
        - IP주소 확인 
        - QR코드 만들기






    - 가상환경
    - 객체지향(나중)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중 상속
        - 추상클래스, 인터페이스


