# 4.	a 리스트에서 중복된 숫자들을 제거하여 출력해 보자
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]

a = [1,1,1,2,2,3,3,3,4,4,5]

set_a = set(a)
#print(set_a)
list_a = list(set_a)
print(list_a)
