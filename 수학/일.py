'''
[Memo...]
len이나 set과 같은 함수는 최대한 지양하는게 좋음..
'''
def one(inp):
    global answers
    n=1
    idx = 1
    while(1):
        if n%inp == 0:
            answers.append(idx)
            break

        n = n + 10**idx
        idx += 1

answers = []
while (1):
    try:
        x = int(input())
    except:
        break

    one(x)

for answer in answers:
    print(answer)