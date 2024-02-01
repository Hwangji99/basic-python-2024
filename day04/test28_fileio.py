# date : 2024-02-01
# test28_fileio.py
# desc : 텍스트 파일 입출력

# mode : a(append : 내용추가) r(read : 파일 읽기) w(write : 파일쓰기) # 이것만 생각
# encoding : cp949(euc-kr : 한글 - 한글이랑 영어만 됨), utf-8(만국공통어 - 다 됨)
f = open('sample.txt', mode='w', encoding='utf-8') # open('파일이름', 모드, 인코딩)
# 뭔가를 한다. write()에서 엔터를 추가하려면 마지막에 \n을 추가해줘야함
f.write('안녕하세요. 우리는 IoT개발자 과정입니다.\n') # mode = a, w일 때만 사용  # r할 때는 못 씀
f.write('반갑습니다!!\n')

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다.')