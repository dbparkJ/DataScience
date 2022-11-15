# 1.  주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

in_num = int(input('숫자를 입력하시오 >>>'))
def is_odd(in_num) :
    if in_num % 2 == 0 :
        return True
    else:
        return False

if is_odd(in_num) == True :
    print('입력된 숫자는 짝수 입니다')
else:
    print('입력된 숫자는 홀수 입니다')


# 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
input_list = list(map(int, input('숫자를 입력하세요 : 예시) 12 13 14 \n').split()))

from statistics import mean, variance
def num_avg(list_num) :
    avg = mean(list_num)
    return avg

print(f'입력한 숫자의 평균 : {int(num_avg(input_list))}')

# 3. 하나의 문자열를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_smile(str) :
    str = str + ':D'
    return str

str_word = input('아무 글이나 쓰세요 \n')
print(print_with_smile(str_word))

# 4. 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
def print_max(first_num ,second_num, third_num) :
    if first_num > second_num and first_num > third_num :
        print(f"첫번째 입력 하신 {first_num}가 가장 큰 수 입니다")
    elif second_num>first_num and second_num > third_num :
        print(f"두번째 입력 하신 {second_num}가 가장 큰 수 입니다")
    else:
        print(f"세번째 입력 하신 {third_num}가 가장 큰 수 입니다")
first_num = int(input('첫번째 수를 입력하세요 : \n'))
second_num = int(input('두번째 수를 입력하세요 : \n'))
third_num = int(input('세번째 수를 입력하세요 : \n'))

print_max(first_num,second_num,third_num)

# 5. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.


