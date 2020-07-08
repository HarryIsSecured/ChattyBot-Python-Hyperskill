# put your python code here
year = int(input())
if year % 100 == 0 and year % 400 == 0:
    if year % 4 == 0:
        print('Leap')
    else:
        print('Ordinary')
else:
    if year % 4 == 0 and year % 100 != 0:
        print('Leap')
    else:
        print('Ordinary')
