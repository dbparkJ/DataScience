num_list = list(range(1,1000)) # 1~ 1000까지의 수 리스트
result_num = [] #공통수를 담을 리스트
sum_num = 0 #리스트 더할 변수

for i in num_list :
    if i % 3 == 0 :
        result_num.append(i)
    if i % 5 == 0 :
        result_num.append(i)

result_num = set(result_num) #리스트의 중복값 제거

for i in result_num :
    sum_num = sum_num + i
print(sum_num)
