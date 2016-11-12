def pig_latin(input_string):
    '''
    '''
    found_vowel = False
    count = 1
    while(count < len(input_string) and not found_vowel):
        if(input_string[count] in 'aeiou'):
            found_vowel = True
        else:
            count += 1
    first_vowel_index = count
    if(input_string[0] in 'aeiou'):
        result = input_string + "w"
    else:
        result = input_string[first_vowel_index:] + input_string[0:first_vowel_index]
    result += 'ay'
    return result

if(__name__ == '__main__'):
    test_file = open('test_file.txt', 'r')
    for next_line in test_file:
        next_line_words = next_line.split()
        result = ''
        for next_word in next_line_words:
            result += pig_latin(next_word) + ' '
        print(result)
    test_file.close()