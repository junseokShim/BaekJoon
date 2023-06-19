import math

N = int(input())
M = int(input())
fault_button_lst = []
if M > 0:
    fault_button_lst = list(map(int, input().split()))

min_val = abs(100-N)
MAX_VALUE = 1000001

for num in range(MAX_VALUE):
    
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) in fault_button_lst:
            break

        if i == len(num)-1:
            min_val = min(min_val, len(num) + abs(int(num)-N))


print(min_val)
