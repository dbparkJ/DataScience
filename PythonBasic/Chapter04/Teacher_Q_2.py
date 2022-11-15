# 2.	(1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력해 보자.
# 화면출력]
# (1, 2, 3, 4)

num = (1,2,3)
lst = list(num)
lst.append(4)
num = tuple(lst)
print(num)

num = num +(5, )

print(num)