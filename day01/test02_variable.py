# date : 2024-01-29
# desc : 변수설명

# 변수(Variable) - 변하는 수. 파이썬에서는 들어가는 종류나 크기에 제약이 없음(!)
var01 = 10
print(var01)

var01 = 10000000000000000000000000000000000000000000000000000000000000000000
print(var01)

var01 = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 # 보기에서 자동 줄바꿈으로 표시한거
print(var01)

var01 = False
print(var01)

var01 = 'Life is short, You need Python.'
print(var01)

# 단, 변수명을 지정시 아래는 불가
## - 숫자로 시작하거나
## - 공백이 있거나
## - _(언더바)이외의 특수문자가 있으면 안됨
#01var
#var iable
#var-01
#var@#01
var_01 = 00
_var_01 = 2 # 되도록 _로 시작하는 변수는 쓰지말것
