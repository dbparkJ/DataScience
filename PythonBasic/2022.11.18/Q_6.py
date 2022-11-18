def all_gugu(dan):
    if dan.__class__ == str :
        for left_num in range(2,10):
            for right_num in range(1,10) :
                print(left_num*right_num,end='\t')
            print()
    else :
        if dan < 2 or dan > 9 :
            print("2 ~ 9 까지의 수만 입력하시오")
        else :
            for i in range(1,10) :
                print(dan*i,end='\t')
dan = input('원하는 단을 입력하세요 (예: 2, 전체: all) : \n')
if dan == 'all' :
    # dan = str(dan)
    pass
else :
    dan = int(dan)

all_gugu(dan)
