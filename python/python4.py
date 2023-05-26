def find_treasure(arg1):

    for string in arg1:
        if(string == 'treasure'):
            print('found')
            return True
        else:
            print('not treasure')


find_treasure(['treasure', 'not_treasure', 'not_treasure', 'treasure'])

find_treasure(['not_treasure', 'not_treasure', 'treasure', 'treasure'])