def wc(ch):
    count = 0
    for c in ch:
        if(c==" "):
            continue
        count = count+1
    return count

print(wc("Hello Hello"))