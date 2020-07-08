a = int(input())  # Recommended
b = int(input())  # Over
h = int(input())  # Input

if h < a:
    print('Deficiency')
else:
    if h > b:
        print('Excess')
    else:
        print('Normal')
