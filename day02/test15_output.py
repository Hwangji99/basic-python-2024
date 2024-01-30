# date : 2024-01-30
# file : test15_output.py
# desc : 콘솔 출력 포맷양식 String Format

string_1 = '{}'.format(10) # {}위치에 함수 뒤에 들어있는 값을 치환, 원하는 양식으로 표현
print(type(string_1))

name =  '고길동' # input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{}  {}  {}'.format(4000, '만', '빌려주세요')
print(string_3)

# 정수를 문자열포맷
# = : 기호와 숫자를 분리, 02 : 두자리 수를 만들 때 빈자리를 0으로 채우기, d는 정수
# 날짜나 시간만들 때 많이 사용 Ex) 09시 50분, 02월 14일
string_4 = '_____{:=+010d}_____'.format(-100)
print(string_4)

# 실수 문자열포맷 f(기본 소수점 6자리)
# 7.2f 전체 자리수를 7자리로 하되 소수점 뒤는 2자리까지
string_5 = '_____{:7.2f}_____'.format(78.33333333333) # 2f는 소수 둘째자리에서 잘라라는 뜻
print(string_5)

# 파이썬 3.6 이후 도입. format() 함수를 아예 사용안함
val = 78.3333333333
string_6 = f'_____{val:7.2f}_____'
print(string_6)

string_7 = 'hello, world!'
print(string_7.upper()) # upper case 대문자변환
print(string_7.lower()) # lower case 소문자변환
print(string_7.lower().capitalize()) # 문장 시작할 때 맨 앞자만 대문자로

print(string_7.split(',')) #특정한 단어로 자르는 함수 => 리스트로 만듦 => 반복문 사용 가능

string_8 = "Hello, I am GD Go. I am a man. Good Luck for your day."
words = string_8.split(' ') # 공백으로 단어를 자름
print(words)
print(f'문장의 단어 갯수는 {len(words)}개입니다.')
string_9 = 'A10'
print(string_9.isalnum()) # True, string_9이 알파벳과 숫자로 되어있는가
print(string_9.isnumeric()) # False, string_9이 숫자로 되어있는가
string_10 = '10.5' # 소수점은 함수를 만들어서 처리해야 한다 
print(string_10.isdecimal()) # False, string_10이 정수인가

print('안냥' in '안녕하세요') # False, 문장 안에 단어가 있는지 확인



