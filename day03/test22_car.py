# date : 2024-01-31
# file :test22_car.py
# desc : Car 클래스 만들기

class Car:
    Wheel_num = 4
    color = 'Blue'
    __plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전(멤버함수)
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def moveBackward(self):
        print(f'{self.__plate_num}이 우회전합니다.')

    # 생성자를 변경했으니까 변경된 생성자로 호출
    def __init__(self, __plate_num, company, color, gear_type) -> None:
         self.__plate_num = __plate_num
         self.company = company 
         self.color = color
         self.gear_type = gear_type

    def __str__(self) -> str: # print(객체) 출력되는 부분
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다.'
    
    def getPlateNumber(self): # 외부에서는 접근할 수 없도록 막는 조치 # 값을 바꿀 수 없음
        return self.__plate_num
    
    def setPlateNumber(self, new_plateNumber): # 값을 바꿀 수 있게 함
        self.__plate_num = new_plateNumber
        
acient = Car('35버 5412', '현대자동차', '실버', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있다.
print(acient)
print(f'차 번호는 {acient.getPlateNumber()}')
print(f'차 색상은 {acient.color}')
acient.moveForward()

acient.__plate_num = '66악 1234' # 악의적인 의도를 가지고 변경 시 _(언더바) 2개를 하면 못 바꿈 (캡슐화)
print(acient)

acient.__plate_num = '99하 99999' # 초보의 실수
print(acient)
acient.setPlateNumber('11짱 5191') # 클래스에 인정받은 동작으로 값을 바꾸기
print(acient)
# csuv = Car('경남88 1914', '기아자동차', '흰색', '수동')
# print(f'차 번호는 {csuv.plate_num}')