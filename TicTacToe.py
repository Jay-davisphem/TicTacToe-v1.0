def cond(state):
    pieces = [j for i in state for j in i]
    wind1 = state[0][0] == state[1][1] == state[2][2] != '_'
    wind2 = state[0][2] == state[1][1] == state[2][0] != '_'
    winh1 = state[0][0] == state[0][1] == state[0][2] != '_'
    winh2 = state[1][0] == state[1][1] == state[1][2] != '_'
    winh3 = state[2][0] == state[2][1] == state[2][2] != '_'
    winv1 = state[0][0] == state[1][0] == state[2][0] != '_'
    winv2 = state[0][1] == state[1][1] == state[2][1] != '_'
    winv3 = state[0][2] == state[1][2] == state[2][2] != '_'
    diff = abs(pieces.count('X') - pieces.count('O'))
    XpO = pieces.count('X') + pieces.count('O')
    if not(wind1 or wind2 or winh1 or winh2 or winh3 or \
        winv1 or winv2 or winv3):
            if  diff > 1:
                return 'Impossible'
            elif (diff == 1) and (XpO == 9):
                return 'Draw'
            elif (diff <= 1) and (XpO < 9):
                return None
    elif (wind1 or wind2 or winh1 or winh2 or winh3 or \
        winv1 or winv2 or winv3):
            cond1 = wind1 or wind2 or winv2 or winh2
            cond2 = winh1 or winv1
            cond3 = winv3 or winh3
            if diff > 1 or (diff <= 1  and ((cond1 and cond2) or (cond1 and cond3) or (cond2 and cond3) or (cond1 and cond2 and cond3))):
                return 'Impossible'
                
            elif cond1:
                return f"{state[1][1]} wins"
            elif cond2:
                return f"{state[0][0]} wins"
            elif cond3:
                return f"{state[2][2]} wins"
            elif (diff == 1) and (XpO == 9):
                return 'Draw'
            elif (diff <= 1) and (XpO < 9):
                return None

def board(keys):  
    print('---------')
    for i in range(len(keys)):
        print('|', end=' ')
        for j in keys[i]:
            if j == 'X':
                print(j, end=' ')
            elif j == 'O':
                print(j, end=' ')
            elif j == '_':
                print(' ', end=' ')
            else:
                print('', end='')
        print('|')
    print('---------')
def show(state):
    print('TIC TAC TO GAME non-GUI\n'\
        'Author: David Oluwafemi Joshua.\n'\
        'About:\n'\
        'A student Python Developer that studies Computer Engineering at\n'\
       'Obafemi Awolowo University, Ile-Ife, Osun State, Nigeria.\n'\
       'Python 3.8.5 ®2020\n'\
       '23rd September, 2020\n'\
       '\nINSTRUCTIONS\n'\
       '1. The possible points are as follows: ',\
       accept.__doc__,'\n'\
       '2. The coordinates prompt for your choice coordinates.\n')
    pieces = [j for i in state for j in i]
    board(state)
    while not cond(state):
        accept(state)
        board(state)
        if cond(state):
            pass
    print(cond(state))
        
    return
def chang(i, j):
    if j == 3:
        if i == 1:
            i -= 1
            j -= 3
        elif i == 2:
            i -= 2
            j -= 2
        elif i == 3:
            i -= 3
            j -= 1
    elif j == 2:
        if i == 1:
            i = i
            j -= 2
        elif i == 2:
            i -= 1
            j -= 1
        elif i == 3:
            i -= 2
            j = j
    elif j == 1:
         if i == 1:
            i += 1
            j -= 1
         elif i == 2:
            i = i
            j = j
         elif i == 3:
            i -= 1
            j += 1
    return i, j   
def accept(game):
  """
  (1, 3), (2, 3), (3, 3)
  (1, 2), (2, 2), (3, 2)
  (1, 1), (2, 1), (3, 1)
  
  """
  while True:
     try:
      po = [i for j in game for i in j]
      ent = input('Enter the coordinates turn: ')
      if ent.replace(' ', '').isdigit():
          i, j = chang(*[int(i) for i in ent.split()])
          if 0 <= i <= 2 and 0 <= j <= 2:
              if game[i][j] == '_':
                  game[i][j] = 'X' if (po.count('O') - po.count('X')) == 1 else 'O'
                  
                  return None
                  break
              elif game[i][j] == 'O' or the_game[i][j] == 'X':
                  print('This cell is occupied! Choose another one!')     
          else:
              print('Coordinates should be from 1 to 3!')
      else:
          print('You should enter numbers!')  
     except TypeError:
         print("Enter a coordinates separating the x and y with space. i.e. x y")     
intake = list('_________')
the_game = []
for i in range(3):
    the_game.append(intake[3 * i : 3 * (i + 1)])

show(the_game)