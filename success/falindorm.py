def solution(s):
    answer = 1
    idx_lst = []

    for idx in range(len(s)):

        memories = s[:idx+1]
        if s[idx] in memories:
            #s_idx = memories.index(s[idx])
            #if s_idx not in idx_lst: idx_lst.append(s_idx)
            #for si in idx_lst:
            for i in range(idx):
                new_s = s[i:idx+1]
                if new_s == new_s[::-1] and len(new_s)>answer:
                    answer = len(new_s)

    return answer
