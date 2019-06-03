orig = input('Enter a word: ')

if len(orig) > 0 and orig.isalpha():
    first_char = orig[0]
    new_word = orig[1:] + first_char + 'ay'
    print(new_word)
else:
    # do your job
    print('invalid word')

