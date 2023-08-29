from collections import Counter

N = int(input())
words = [input() for _ in range(N)]

num = 9
sum_num = 0
alpha_weight_dict = {}
alpha_to_num_dict = {}

for word in words:
    for i in range(len(word)):
        if word[i] not in alpha_weight_dict:
            alpha_weight_dict[word[i]] = 10**(len(word)-1-i)

        else:
            alpha_weight_dict[word[i]] = alpha_weight_dict[word[i]] + 10**(len(word)-1-i)


alpha_weight_dict = sorted(alpha_weight_dict.items(), key = lambda item: item[1], reverse=True)

for key in alpha_weight_dict:
    alpha_to_num_dict[key[0]] = num
    num -= 1

for word in words:
    s = ''
    for i in range(len(word)):
        s = s + str(alpha_to_num_dict[word[i]])

    sum_num += int(s)

print(sum_num)
