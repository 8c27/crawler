from crawler_.eight_offcial.catch_data import eo

demo = '功能表\ 0)離開\ 1)下載八大官股買賣超'

while True:
    option = input(demo+'   請輸入功能代號: ' )
    if option == '0':
        exit()
    elif option == '1':
        print(eo())
