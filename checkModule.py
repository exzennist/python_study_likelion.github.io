def adultCheck(): 
    try : 
        age = int(input("나이를 입력하세요"))

        if age <=19 : 
            print("구입할 수 없습니다.")
        else : 
            print("구매 완료")
    except ValueError : 
        print("Error")
