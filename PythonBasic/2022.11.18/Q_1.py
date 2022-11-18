def my_div(num1, num2) :
    try :
        div_value = num1 / num2
        portion = num1 // num2
        rest = num1 % num2
    except Exception as e :
        print(e)

    return div_value, portion, rest


first_num =  int(input('첫번째 수를 입력하세요 : '))
second_num =  int(input('두번째 수를 입력하세요 : '))

print(my_div(first_num, second_num))
"""
두 수를 입력 받아야 한다
first_num =  input('첫번째 수를 입력하세요 : ')
second_num =  input('두번째 수를 입력하세요 : ')


리턴값 
나눈 값 :
몫 :
나머지 :
분모가 0일 경우 예외 처리를 한다.
"""