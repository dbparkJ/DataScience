def StarCount(height) :
    # 층수, 별수 변수 선언
    h_cnt = s_cnt = 0

    while h_cnt < height :
        h_cnt += 1
        print('*'*h_cnt)
        s_cnt += h_cnt
    return s_cnt

height = int(input('height : '))
print('star 개수 : %d'%StarCount(height))