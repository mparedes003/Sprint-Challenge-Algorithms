'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#word = 'wahtTHrthmth'


def count_th(word):

    # BASE CASE
    # If it is an empty string
    if word == '':
        # return 0 for false
        return 0

    else:
        # if word contains the string 'th'
        if word[0:2] == 'th':
            # return 1 and increment 2 indecies and recursively run the function
            return 1 + count_th(word[2:])
        else:
            # do not return anything and increment 1 index and recursively run the function
            return count_th(word[1:])

    # print(count_th(word))
