def wc2(chars):
    word_count = 0
    char_count = 0
    whitespace_count = 0
    word_flag = False

    for char in chars:
        if char == ' ':
            whitespace_count = whitespace_count+1
            word_flag = False
            continue
        char_count = char_count +1
        if word_flag == False:
            word_count = word_count+1
            word_flag = True   
    return word_count, char_count, whitespace_count

print(wc2(" 안녕하세요? 하하 조금씩, 꾸준히, 아주 작은 실천으로 시작하는  나다운 하루")) 
        