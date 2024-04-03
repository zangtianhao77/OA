def subseq (source, target):
    set_source = set(source)
    set_target = set(target)
    for x in set_target:
        if x not in set_source:
            return -1

    count = 0
    i = 0
    while i < len(target):
        sub = ""
        for ch in source:
            if i < len(target) and ch == target[i]:
                sub +=ch
                i+=1

        count+=1


    return count



print(subseq("abc", "acbcc")) #ac + bc + c -> 3

