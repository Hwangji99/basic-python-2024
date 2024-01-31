# date : 2024-01-31
# file : test17_input.py
# desc : 콘솔 입력

# input()
# 출력 - 컴퓨터 화면, 프린터, 스피커, 빔 프로젝터, VR, ...
# 입력 - 콘솔 입력(키보드), 마우스 입력, 목소리, 조이스틱, 터치스크린 
# input('내용추가')   # () 안에 내용을 반드시 추가해야 한다.

temp_val = input('곱할 수 입력 -> ') 
if temp_val.isnumeric() == True: # 숫자 입력이 아니면 튕겨내기
    temp_val = int(temp_val) # [문자열]에서 [정수]로 변환(형변환) -> 결과가 [문자]에서 [숫자]로 바뀌어 나온다
    print(f'입력값 = {temp_val}')

    # 곱하기
    result = temp_val * 5
    print(f'결과 = {result}')
else:
    print('잘못된 입력, 정수만 입력하세요.')
