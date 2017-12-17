def step1(programs, moves):
    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            programs = programs[-x:] + programs[:-x]
        else:
            if move[0] == 'x':
                a = int(move[1:move.index('/')])
                b = int(move[move.index('/') + 1:])
            else:
                assert move[0] == 'p'
                a = programs.index(move[1])
                b = programs.index(move[3])
            programs = programs[:min(a, b)] + \
                    programs[max(a, b)] + \
                    programs[min(a, b) + 1:max(a, b)] + \
                    programs[min(a, b)] + \
                    programs[max(a, b) + 1:]
    return programs


programs = 'abcdefghijklmnop'
moves = input().strip().split(',')
print(step1(programs, moves))
