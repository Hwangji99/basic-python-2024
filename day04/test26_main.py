# date : 2024-02-01
# test26_main.py
# desc : __main__ 에 대한 내용

class Temp:
    pass

if __name__ == '__main__': # __name__는 스페셜 변수
    print('제가 시작점입니다.')
    tt = Temp() 
    print(type(tt)) # main = 시작점 = 엔트리 포인트