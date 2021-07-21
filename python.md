## boolearn
boolearn : 참 / 거짓 
```py
print(5>10) # False
print(True) # True
print(not False) # True
print(not 10>5) # False
```
---
## 변수 
* 정수형은 문자열인 (str)로 감싸줘야 한다. 
* 중간에 변수를 바꾸면 바뀐 변수값으로 적용이 된다.
* '+' 가 아닌 ','로 연결할 수 있다. 이 경우는 정수를 문자열로 바꾸지 않아도 되지만, 띄어쓰기가 포함되어 출력된다. 
```py
# 변수 선언
animal ="강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3

print("우리집" + animal + "의 이름은" + name + "이다.")
print(name + "는" + str(age) + "살이고," + hobby + "을 좋아한다.")
print(name +"는 어른일까?" + str(is_adult))

# 우리집 강아지의 이름은 연탄이 이다. 
# 연탄이는 4살이고 산책을 좋아한다. 
# 연탄이는 어른일까? True
```

#### 퀴즈
* 변수를 이용하여 다음 문장을 출력해라 
    * 변수명  : station
    * 변수값 : "사당", "신도림", "인천공항" 순서대로 입력 
    * 출력문장 : xx 행 열차가 들어온다. 
```py
station ={'사당', '신도림', '인천공항'}

for i in station : 
    print(i + '행 열차가 들어오고 있습니다.')

# 사당 행 열차가 들어오고 있습니다.
# 신도림 행 열차가 들어오고 있습니다.
# 인천공항 행 열차가 들어오고 있습니다.
```
---
<!--주석-->
## 주석
* '#'
* 작은 따옴표 앞뒤로 3개 
* ctrl + / : 여러문장 한번에 주석
```py
# 주석이다.

'''주석
이다
'''
```

---
<!--연산자-->
## 연산자 

### 1. 연산자
```py
print(1+1) #2
print(3-2) # 1
print(3*2) # 6
print(6/3) # 2

print(2**3) # 8 # 제곱
print(5%3) # 2 # 나머지
print(5//3) # 1 # 몫

print(10 >=7) # True
print(3==3) # True
print(1 != 3) # True
print(not(1!=3)) # False

print((3>0) and (3<5)) # True
print((3>0) & (3>5)) # True

print((3>0) or (3>5)) # False
print((3>0) | (3>5)) # False

print(5>4>7) # False
```
### 2. 수식
```py
print(2+3*4) # 14
print((2+3)*4) # 20

number = 2+3*4
print(number) # 14

number = number + 2  
print(number) # 16

number += 2 
print(number) # 18

number *= 2
print(number) # 36
```
### 3. 숫자처리 함수 
* 숫자처리 함수 
    * abs() : 절대값 
    * pow() : 제곱
    * max(), min() : 최대, 최소 
    * round() : 반올림 
```py
print(abs(-5)) #5
print(pow(4,2)) # 16
print(max(5,12)) # 12
prnt(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5
```
* math 라이브러리 사용하기 
    * floor() : 반내림 
    * ceil() : 반올림 
    * sqrt() : 제곱근 (루트)
```py 
from math import * 
print(floor(4.99)) # 4 
print(ceil(3.14)) # 4
print(sqrt(16)) # 4
```
### 4. 랜더 함수 
* random() : 0.0이상 1.0 이하
```py
form random import * 

print(random()) # 0.0 ~ 1.0 사이의 임의의 값 생성 
print(random() * 10) # 0.0 ~ 10.0 사이의 임의의 값 생성 

print(int(random()*10) # 0 ~ 10 사이의 임의의 값 생성 
print(int(random()*10 + 1)) # 1이상  10 이하의 임의의 값 생성 

# 로또 번호 출력 하기 (1~45)
print(random() * 45 + 1) # 1~ 45 이하의 임의의 값 생성 
```
</br>

* randrange(x, y) : x이상 y미만의 임의의 값 생성
```py 
from random import * 

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성 
```
</br>

* randint(x,y) : x이상 y이하의 임의의 값 생성
```py
from random import * 

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
```
</br>

#### 퀴즈 
* 월 4회 스터디를 하는데 3번은 온라인, 1번은 오프라인이다. 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성해라. 
    * 조건1 : 랜덤으로 날자를 뽑는다. 
    * 조건2 : 월별 날짜는 최소일수인 28일 이내로 정한다. 
    * 조건3 : 매월 1~3일은 스터디를 주니해야 하므로 제외한다. 
    * 출력문 예제 : "오프라인 스터디 모임 날짜는 매월 x 일로 선정되었다."

```py
from random import * 
date=randint(4,28)

print("오프라인 스터디 모임 날짜는 매월" + str(date) + "로 선정되었다.")
```
```py
from random import * 
date=randrange(4,29)

print("오프라인 스터디 모임 날짜는 매월" + str(date) + "로 선정되었다.")
```
```py
from random import * 
date=int(random()*28+4)

print("오프라인 스터디 모임 날짜는 매월" + str(date) + "로 선정되었다.")
```
---
<!--문자열 처리-->
# 문자열 처리 

### 1. 문자열
```py
sentence ="나는 소년이다."
print(sentence) # 나는 소년이다. 

sentence2 ="""
나는 
소년
이다.
"""
print(sentence2) #나는/n 소년/n 이다.
```
### 2. 슬라이싱 
* 슬라이싱 : 문자열에 번호를 매겨 출력하고 싶은 부분을 선택한다. 
```py
jumin="990120-1234567"
# 번호 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
# 번호 : -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1

print("성별:" + jumin[7]) # 성별 : 1

print("연:" + jumin[0:2]) # 연 : 99
print("월 : " + jumin[2:4]) # 월 : 01
print("일 : " + jumin[4:6]) # 일 : 20

print("생년월일 : " jumin[:6]) # 생년월일 : 991012
print("뒤 7자리 : " jumin[7:]) # 뒤 7자리 : 1234567

print("뒤 7자리 : " jumin[-7:]) # 뒤 7자리 : 1234567
```
### 3. 문자열 처리함수 
* .lower() : 소문자
* .uppser() : 대문자
* .isupper() : 해당 문자가 대문자인가요?
* len() : 길이 
* .replace(x,y) : x를 y로 바꾼다. 
```py
python ="Python is Amazing" 

print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True

print(len(python)) # 17 
print(python.replace("Python","Java")) # Java is Amazing
```
</br>

* .index() : 문자열에서 해당 문자의 위치 (오류 o)
* .find() : 문자열에서 해당 문자의 위치 (오류x)
* .count() : 해당 문자의 개수 
```py
index = python.index("n")
print(index) # 5

index = python.index("n", index+1)
print(index) # 15
print(python.index("Java")) # 오류 

print(python.find("n")) # 5 포함된 위치 알려줌
print(python.find("Java")) # 없으면 -1

print(python.count("n")) # 2 n이 몇번나왔나 
```
### 4. 문자열 포맷
* % 
    * %d : 숫자
    * %s : 문자열
    * %c : 문자
```py
print("나는 %d살이다." % 20) # 나는 20살이다. 
print("나는 %s을 좋아해" % "파이썬") #나는 파이썬을 좋아해 
print("Apple은 %c로 시작해" % "A") #Apple은 A로 시작해
print("나는 %s 색과 %s색을 좋아해" % ("파란", "빨간")) #나는 파란색과 빨간색을 좋아해 
```
</br>

* .format 
```py
print("나는 {}살이다.".format(20))
print("나는 {} 색과 {}색을 좋아해".format("파란", "빨간"))
print("나는 {0} 색과 {1}색을 좋아해".format("파란", "빨간"))
print("나는 {1} 색과 {0}색을 좋아해".format("파란", "빨간"))
```
</br>

* .format 변수 
```py
print("나는 {age}살이며, {color}색을 좋아해".format(age=20, color="보라"))
```
</br>

* 변수 f
```py
age=20
color="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해")
``` 
## 5. 탈출문자 
* \n : 줄바꿈
* \" \" : 큰 따옴표 
* \ \ : 역슬래시 1개 '\'
* \r : 커서를 맨 앞으로 이동 
*  \b : 백스페이스(한 글자 삭제)
* \t 탭

```py
#\n
print("안녕\n 그래")
'''안녕
그래'''

#\" \"
print("안녕 \"그래\" 안녕")
#안녕 "그래" 안녕

# \\
print("안녕 \\ 그래 \\ 안녕")
# 안녕 \ 그래 \ 안녕

#\r : 커서를 맨 앞으로 이동 
print("Red Apple\r Pine")
# Pine Red Apple

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")
# Red Apple

# \t 탭 
print("Red\t Apple")
# Red    Apple
```
#### 퀴즈 
* 사이트별로 비밀번호를 만들어주는 프로그램을 작성하라.
    * 예) http://naver.com
    * 규칙 1 : http:// 부분 제외 => naver.com
    * 규칙 2  : 처음 만나는 점(.) 이후 부분은 제외 => naver
    * 규칙 3 : 남은 글자 중 처음 세자리(nav) + 글자 개수(5) + 글자 내 'e' 개수(1) + "!"로 구성

```py
url="http://naver.com"
# 규칙 1  : naver.com
my_str=url.replace("http://","")

# 규칙 2 : naver
my_str=my_str[:my_str.index(".")]

# 규칙  3 : nav51!
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0}의 비밀번호는 {1}이다.".format(url, password))
# http://naver.com의 비밀번호는 nav51!이다.

```
---
<!--자료구조-->
# 자료구조 
## 1. 리스트 
* [] : 리스트 
    * .append() : 리스트 맨 뒤에 추가 
    * .insert(1,"x") : 1번째에 x 추가
    * .pop() : 맨 뒤 삭제
    * .sort() : 오름차순 정렬 
    * .reverse() : 내림차순 정렬
    * .clear : 전체 삭제
    * .extend() : 리스트 확장(합침)
```py
# 지하철 칸별로 10명, 20명, 30명 
subway1 = 10
subway2 = 20
subway3 = 30 

subway=[10,20,30]
print(subway) # [10 20 30]

subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']

# 조세호씨가 몇번째 칸에 타고있는가?
print(subway.index("조세호")) # 1 

# 맨뒤에 하하가 탐 .append()
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 탐 
subway.insert(1,"정형돈") #['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람들을 한명씩 뒤에서 내림 
print(subway.pop()) # 하하
print(subway) #['유재석', '정형돈', '조세호', '박명수']

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석") #['유재석', '정형돈', '조세호', '박명수', '유재석']
print(subway.count("유재석")) # 2

# 정렬 
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기 
num_list.clear
print(num_list) # []

# 다양한 자료형과 함께 사용 가능
mix_list=["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

# 리스트 확장 (합치기)
num_list.extend(mix_list) 
print(num_list) # [5, 4, 3, 2, 1, '조세호', 20, True ]
```
## 2. 딕셔너리 (사전)
* {key, "value"} : 딕셔너리 
```py
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호 

print(cabinet.get(3)) # 유재석
```
</br>

* 오류 
```py
# 오류
print(cabinet[5]) # 오류 (이후 코드 출력 불가)
print(cabinet.get(5)) # 오류가 나도 프로그램 지속 (이후 코드 출력 가능)

print(cabinet.get(5, "사용가능")) # 사용가능 (딕셔너리에 없으면 해당 문구를 출력한다.)
```
</br>

* 값 존재 여부 
```py
# 값이 있는지 없는지 확인한다. 
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : 유재석, "B-100" : 김태호"}
```
</br>

* 값 추가, 삭제 
    * del : 삭제 
    * .clear() : 전체 삭제 
    * .keys() : key 값 출력 
    * . values() : Value 값 출력
    * .items() : key, value 모두 출력 
```py
# 새 손님 업데이트
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet) # {'A-3' : 김종국, 'B-100' : '김태호', 'C-20' : '조세호' }

# 삭제 
del cabinet["A-3"]
print(cabinet) # {'B-100' : '김태호', 'C-20' : '조세호' }

# key, value 출력 
print(cabinet.keys()) # dic_keys(['B-100', 'C-20'])
print(cabinet.values()) # dict_values(['김태호', '조세호'])
print(cabinet.itmes()) # dict_item('B-100', '김태호', 'C-20', '조세호')

# 모든 값 삭제 
cabinet.clear()
print(cabinet) #{}
```
### 3. 튜플 
* ( )
```py
menu=("돈까스")
print(menu[0]) 
print(menu[1])

(name, age, hobby) = ("김종국", 20, "코딩")
print( name, age, hoppy) # 김종국 20 코딩
```
### 4. 세트 
* { } : 세트(집합)
* set()
* 중복x, 순서x
    * 교집합  : & , .intersection
    * 합집합 : | , .union
    * 차집합 : - , .difference
    * 추가 : .add
    * 뺌 : .remove

```py 
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}


java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 
print(java & python) # {'유재석'} 
print(java.intersection)  # {'유재석'} 

# 합집합
print(java | python) # {'김태호', '박명수', '유재석', '양세형}
print(java.union(python)) # {'김태호', '박명수', '유재석', '양세형}

# 차집합 (java만 할 수 있는 사람)
print(java-python) # {'김태호', '양세형}
print(java.difference(python)) # {'김태호', '양세형}

# python 을 할 수 있는 사람이 늘어남
python.add("김태호")
print(python) # {'김태호', '박명수', '유재석'}

# java에서 김태호 빠짐
java.remove("김태호")
print(java) # {"유재석", "양세형"}
```

### 5. 자료구조 변경 
```py
menu = {"커피", "우유", "주스"}
print(menu) # {"커피", "우유", "주스"}
print(menu, type(menu)) # {'커피', '주스', '우유'} <class 'set'>

menu=list(menu)
print(menu, type(menu)) # ['커피', '주스', '우유'] <class 'list'>

menu=tuple(menu)
print(menu, type(menu)) # ('커피', '주스', '우유') <class 'tuple'>
```
#### 퀴즈 
* 댓글 작성자들 중 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받는다. 추첨 프로그램을 작성해라 
    * 조건 1 : 20명이 작성했고, 아이디는 1~20이라고 가정한다. 
    * 조건 2 : 댓글 내용과 상관없이 무작워로 추첨하되 중복 불가 
    * 조건 3 : random 모듈의 shuffle 과 sample 을 사용한다. 
```py
from random import * 
lst=[1,2,3,4,5]
# shuffle : 랜덤으로 순서 재배열
shuffle(list) #[3,5,1,4,2]

# sample : 랜덤으로 원하는 개수만큼 추출
print(sample(lst,1)) #[3]
```
* 출력 예제 
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
--축하합니다.--
```py
from random import * 
users = range(1,21) # 1~20 
#print(type(users)) <class 'range'>
users=list(users)

shuffle(users)
# 4명을 먼저 뽑고 1명은 치킨, 3명은 커피
winners=(sample(users,4))

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")
```
---
<!--제어문-->
# 제어문

## 1. if
```py
weather = input("오늘 날씨 어때요?")
if weather =="비":
    print("우산 챙겨요")
elif weather == "미세먼지" : 
    print("마스크 챙겨요")
else : 
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("더워요")
elif 0 <= temp <10 : 
    print("쌀쌀")
else : 
    print("추워")
```
## 2. for 반복문
* for : 정해진 횟수가 있음 
    * 운동장 10바퀴 돌아. 
```py
# 리스트
for waiting_no in [1,2,3,4,5]:
    print("대기번호 : {0}".format(waiting_no))
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5

# range()
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
# 대기번호 : 0
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4

# randrange()
for waiting_no in randrange(1,6):
    print("대기번호 : {0}".format(waiting_no))

starbucks=["김", "이", "박","최"]
for customer in starbucks : 
    print("{0}, 커피받아라".format(customer))
# 김, 커피받아라
# 이, 커피받아라
# 박, 커피받아라
# 최, 커피받아라
```
## 3. while 반복문 
* while : 정해진 조건이 있음 
    * 기록 1초 단축될 때까지 돌아 
```py 
customer = "가" 
index = 5 

while index >= 1 : 
    print("{0}, 커피 받아라. {1}번 남았다.".format(customer, index) )

    if index == 0 : 
        print("커피 버림")
```
* 무한 루프 
```py 
customer ="나"
index = 1

while True : 
    print("{0}, 커피 받아라. 호출 {1} 회".format(customer, index))
    index += 1 

```
```py
customer = "다"
person = "Unknown"

# customer이 "다"가 아니면 계속 이름 뭐냐고 물어봄
while person != customer : 
    print("{0}, 커피 받아.". format(customer))
    person = input("이름 뭐야")
```
## 4. continue, break
* continue : 반복문 계속 진행 
* break : 반복문 멈춤
```py 
# 결석생
absent = [2,5]

for student in range(1,11) # 출석번호 1 ~ 10 
    if student in absent : 
        continue
     print("{0}, 책 읽어.".format(student))
# 1, 책 읽어.
# 3, 책 읽어.
# 4, 책 읽어.
# 6, 책 읽어.
# 7, 책 읽어.
# 8, 책 읽어.
# 9, 책 읽어.
# 10, 책 읽어.

# break 
absent = [2,5] # 결석 
no_book = [7] # 책 안가져옴 

for student in range(1,11) : # 출석번호 1 ~ 10 
    if student in absent : 
        continue
    elif student in no_book : 
        print("{0}, 때문에 오늘 수업 끝낸다. ".format(student))
        break
    print("{0}, 책 읽어.".format(student))

# 1, 책 읽어.
# 3, 책 읽어.
# 4, 책 읽어.
# 6, 책 읽어.
# 7, 때문에 오늘 수업 끝낸다.
```
## 5. 한 줄 for
```py 
# 출석번호 앞에 100을 붙이기로 함 => 101, 102, 103, 104
students = [1, 2, 3, 4, 5]

students = [i + 100 for i in students] 
print(students) # [101, 102, 103, 104, 105]

# 학생이름을 길이로 변환 
students = ["PineApple man", "Grape man", "Peach man"]
students = [len(i) for i in students]
print(students) # [13, 9, 9]

# 학생 이름 대문자로 변한 
students= [i.upper() for i in students]
print(students) #['PINEAPPLE MAN', 'GRAPE MAN', 'PEACH MAN']
``` 
#### 퀴즈 
* 50명의 승객과 매칭기회가 있다. 총 탑승 승객 수를 구하는 프로그램 작성하라. 
    * 조건 1 : 승객별 운행 소요 시간 5분 ~ 50분 사이의 난수이다. 
    * 조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 한다. 

* 출력문 예제 
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분 
```py 
from random import * 

cnt = 0 # 총 승객 수 초기값 

for i in range(1, 51): # 1 ~ 50 총 승객
    time = randrange(5, 51) # 조건 1 : 승객별 운행 소요 시간 5분 ~ 50분 사이의 난수이다. 
    if 5 <= time <= 15 : #조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 한다. 
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        cnt +=1
    else : 
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}".format(cnt))

# [ ] 1번째 손님 (소요시간 : 43분)
# [O] 2번째 손님 (소요시간 : 6분)
# [ ] 3번째 손님 (소요시간 : 39분)
# [ ] 4번째 손님 (소요시간 : 45분)
# [ ] 5번째 손님 (소요시간 : 38분)
# [O] 6번째 손님 (소요시간 : 11분)
# [ ] 7번째 손님 (소요시간 : 23분)
# [ ] 8번째 손님 (소요시간 : 36분)
# [ ] 9번째 손님 (소요시간 : 47분)
# [ ] 10번째 손님 (소요시간 : 43분)
# [ ] 11번째 손님 (소요시간 : 48분)
# [ ] 12번째 손님 (소요시간 : 27분)
# [ ] 13번째 손님 (소요시간 : 49분)
# [ ] 14번째 손님 (소요시간 : 44분)
# [ ] 15번째 손님 (소요시간 : 41분)
# [ ] 16번째 손님 (소요시간 : 45분)
# [ ] 17번째 손님 (소요시간 : 22분)
# [O] 18번째 손님 (소요시간 : 7분)
# [O] 19번째 손님 (소요시간 : 5분)
# [ ] 20번째 손님 (소요시간 : 22분)
# [ ] 21번째 손님 (소요시간 : 36분)
# [ ] 22번째 손님 (소요시간 : 33분)
# [ ] 23번째 손님 (소요시간 : 16분)
# [ ] 24번째 손님 (소요시간 : 17분)
# [O] 25번째 손님 (소요시간 : 15분)
# [ ] 26번째 손님 (소요시간 : 29분)
# [ ] 27번째 손님 (소요시간 : 24분)
# [O] 28번째 손님 (소요시간 : 13분)
# [ ] 29번째 손님 (소요시간 : 40분)
# [ ] 30번째 손님 (소요시간 : 50분)
# [ ] 31번째 손님 (소요시간 : 43분)
# [ ] 32번째 손님 (소요시간 : 24분)
# [O] 33번째 손님 (소요시간 : 6분)
# [ ] 34번째 손님 (소요시간 : 43분)
# [ ] 35번째 손님 (소요시간 : 26분)
# [O] 36번째 손님 (소요시간 : 12분)
# [ ] 37번째 손님 (소요시간 : 43분)
# [ ] 38번째 손님 (소요시간 : 39분)
# [ ] 39번째 손님 (소요시간 : 42분)
# [ ] 40번째 손님 (소요시간 : 31분)
# [ ] 41번째 손님 (소요시간 : 41분)
# [ ] 42번째 손님 (소요시간 : 30분)
# [ ] 43번째 손님 (소요시간 : 34분)
# [ ] 44번째 손님 (소요시간 : 18분)
# [ ] 45번째 손님 (소요시간 : 28분)
# [ ] 46번째 손님 (소요시간 : 21분)
# [ ] 47번째 손님 (소요시간 : 49분)
# [O] 48번째 손님 (소요시간 : 8분)
# [ ] 49번째 손님 (소요시간 : 29분)
# [O] 50번째 손님 (소요시간 : 14분)
# 총 탑승 승객 : 10
---