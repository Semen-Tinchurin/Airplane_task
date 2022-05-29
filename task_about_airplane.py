

n = int(input('Enter a number of tickets: '))
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']
TOTAL = 119


def checking(n):
    if n == TOTAL:
        print('full')
    else:
        places_list = ['1D', '1E', '1F']
        for i in range(2, 21):
            for j in LETTERS:
                places_list.append(str(i) + j)
        places_list.append('21D')
        places_list.append('21E')
        print(places_list[n])


checking(n)
