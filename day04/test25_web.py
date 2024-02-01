# date : 2024-02-01
# test25_web.py
# desc : urllib 모듈 사용법

# 명령 프롬프트에  pip install requests를 입력했는데 Successfully가 떠야 업데이트 된 것

#  from urllib.request import *     # request 안에 모든 걸 쓰고 싶다면 *를 넣으면 된다
from urllib.request import Request, urlopen # Request 클래스와 urlopen만 쓰겠다는 의미

req = Request('https://www.naver.com/') # 네이버 웹주소(url)
res = urlopen(req) # url주소로 웹사이트를 열어달라고 요청

print(f'응답코드 : {res.status}') # url로 요청된 웹사이트 응답 확인 # 200대가 성공한 것(소스를 끌고 올 수 있음) # 400대는 오류

print(res.read()) # 네이버 홈페이지 코딩  # read는 해당 코딩을 가져온다 

# urllib.request보다 성능이 조금 더 나은 모듈. pip install 설치해야함
import requests

res2 = requests.get('https://www.naver.com/') # requests는 모듈, get은 함수 # 마찬가지로 네이버의 데이터를 가져온다

print(res2.status_code)
print(res2.text) 