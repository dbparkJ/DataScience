def gugu(dan):
    if dan < 2 or dan > 9 :
        print("2 ~ 9 까지의 수만 입력하시오")
    else :
        for i in range(1,10) :
            print(dan*i,end='\t')


dan = int(input('원하는 단을 입력하세요 : \n'))
gugu(dan)
