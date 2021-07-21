# 파이썬 1주차 과제 

from random import *

a = randint(1, 6)
b = randint(1, 6)

print("주사위 던지기")
print("주사위 1: {0}".format(a))
print("주사위 2: {0} \n".format(b))


print("실행할 연산의 종류를 입력하세요.")
print('1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 나머지 구하기')
type = input("연산종류 : ")

result = 0 # result는 정수형이기 때문에 문자열로 변환해야 함

if type == "1" : 
    result = a+b
    print("덧셈 결과 : " + str(result))

elif type == "2" : 
    result = a-b
    print("뺄셈 결과 : " + str(result))

elif type == "3" : 
    result = a*b
    print("곱셈 결과 : " + str(result))

elif type == "4" : 
    result = a/b
    print("뺄셈 결과 : " + str(result))

elif type == "5":
    result = a%b
    print("나머지 구하기 결과 : " + str(result))

# 별찍기 
for i in range(result):
    if i <= result : 
        print("*" * i) 
        i +=1

# 1~5 이외의 값을 입력했을 때 다시 "연산 종류 : " 을 출력하게하려면 어떻게 해야 할까요?
# 주사위 2개가 같은 값이 나올경우, 뺄셈은 0이 되어 별이 출력되지 않는다. 주사위 2개를 각각 다른 문자가 나오게 하려면 어떻게 해야 할까?
