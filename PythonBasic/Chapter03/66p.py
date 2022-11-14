numData = []

while True :
    num = int (input("숫자입력 : "))

    if num % 10 == 0:
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)