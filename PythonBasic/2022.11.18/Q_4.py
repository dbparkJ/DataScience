"""
random 모듈 사용
로또번호는 1 ~ 45


"""
import random

lotto_num_list = list(range(1,46))
lotto_num = random.sample(lotto_num_list, 6)
lotto_num.sort()

print(lotto_num)
