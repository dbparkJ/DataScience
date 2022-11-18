def getTotalPage(m, n) :
    page_cnt = 0
    page_cnt = m // n +1

    if m % n == 0 :
        page_cnt = page_cnt - 1

    return page_cnt

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
