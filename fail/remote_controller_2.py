N = int(input())
M = int(input())

button_lst = [e for e in range(10)]
if M > 0:
    fail_button_lst = [int(e) for e in input().split(" ")]
    button_lst = [e for e in button_lst if e not in fail_button_lst]


def isFailed(current_num):
    isFail = False
    for e in list(str(current_num)):
        if int(e) not in button_lst:
            isFail = True
            return isFail
    return isFail


isFail = False
c = 0

max_val = 0
current_num = 100

if N>current_num:

    while 1:
        if current_num >= N and isFailed(current_num) == 0: 
            if abs(current_num-N) <= abs(max_val-N): max_val = current_num
            else: max_val = max_val
            break
        
        isFail = isFailed(current_num)

        if isFail == False:
            max_val = max(max_val, current_num)

        current_num += 1
        isFail = False

    c = len(str(max_val))+abs(N-max_val)


elif N<current_num:
    
    while 1:
        if current_num <= N and isFailed(current_num) == 0: 
            if abs(current_num-N) <= abs(max_val-N): max_val = current_num
            else: max_val = max_val
            break
        
        isFail = isFailed(current_num)

        if isFail == False:
            max_val = max(max_val, current_num)

        current_num -= 1
        isFail = False 

    c = len(str(max_val))+abs(N-max_val)

c = min(c, abs(100-N))
print(c)