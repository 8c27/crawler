from crawler_.crawler_lib.big_eight import big_eight_price

demo = '功能表\ 0)離開\ 1)下載八大官股買賣超'

while True:
    option = input(demo+'   請輸入功能代號: ' )
    if option == '0':
        exit()
    elif option == '1':
        print(big_eight_price())
