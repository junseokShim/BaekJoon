from itertools import combinations

inputs = []
answers = []

while 1:
    answer = []
    lst = list(input().split(" "))
    k = lst[0]
    if int(k) == 0: break
    new_lst = list(map(int, lst[1:]))
    
    for l in list(combinations(new_lst, 6)):
        answer.append(list(l))

    answers.append(answer)
        
for answer in answers:
    for e in answer:
        print(' '.join(map(str,sorted(e))))
    print()
    