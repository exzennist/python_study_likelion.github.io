# 클래스 상속과 오버라이딩 개념을 이용하여 아래에 제시된 클래스 정의 
# 부모클래스 : Shape (넓이를 계산하는 area 메서드를 가짐. 반환값 0)
# 자식 클래스 : Squre (정사각형 한변의 길이를 나타내는 length 필드 추가로 가짐. 
# 기존 Shape클래스의 area 메서드를 정사각형 넓이를 계산해 반환하는 메서드로 오버라이딩 )

# 정사각형의 한 변의 길이를 입력받은 뒤, 입력받은 값을 변의 길이로 하는 정사각형의 넓이 출력 

# 실행 예시 
# 정사각형의 한 변의 길이를 입력하세요 : 5
# 정사각형의 면적 : 25

class Shape :
    def __init__(self, length):
        self.length = length

    def area (self) : 
        return 0

class Squre(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)

    def area(self,length) :
        area = self.length**2
        print("정사각형의 면적 : {0}".format(area))
        return area

len = int(input ("정사각형의 한 변의 길이를 입력하세요 : "))
result = Squre(len)
result.area(len)
