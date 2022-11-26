global d
d = [['-','-','-'],['-','-','-'],['-','-','-']]
winner = 0
HowManyMoved =0
print()


def boxes():
  for x in range(3):
    print(' '.join(d[x]))
def X(r,c):
  d[r][c] = 'X'
def O(r,c):
  d[r][c] = 'O'  
  
def processX():
  global HowManyMoved
  rows = input("Player X: Which row (1,2,3):")
  rows = int(rows)
  column = input("Player X: Which column (1,2,3):")
  column = int(column)
  if d[rows-1][column-1] == '-':
    X(rows-1, column-1)
    HowManyMoved = HowManyMoved + 1
  else:
    print("Please enter X in a blank spot")
  boxes()

def processO():
  global HowManyMoved
  rows = input("Player O: Which row (1,2,3):")
  rows = int(rows)
  column = input("Player O: Which column (1,2,3):")
  column = int(column)
  if d[rows-1][column-1] == '-':
    O(rows-1, column-1)
    HowManyMoved = HowManyMoved + 1
  else:
    print("Please enter O in a blank spot")

def output():
  
  strX = 'X'
  strO = 'O'
  global winner
  global d

  #TODO: the below 3 linese doesn't work
  #d[0][0] == 'X'
  #d[0][1] == 'O'
  #d[0][2] == 'X'
  
  #Insert Test Data
  """
  O(0,0)
  O(0,1)
  O(0,2)

  boxes() # print out the d arrays
  """

  winner = 0
  if d[0][0] == d[0][1] == d[0][2]:
    winnerRow = 0
    winnerCol = 0
    
  if d[1][0] == d[1][1] == d[1][2]:
    winnerRow = 1
    winnerCol = 0
    
  if d[2][0] == d[2][1] == d[2][2]:
    winnerRow = 2
    winnerCol = 0


  StrWinner = d[winnerRow][winnerCol]

  if StrWinner == "X"
    winner = 1
  if StrWinner == "O"
    winner = 2 
  
  
  if d[0][0] == d[1][0] == d[2][0]:
    if d[1][0] == strX:
      winner = 1
    if d[1][0] == strO:
      winner = 2
  if d[0][1] == d[1][1] == d[2][1]:
    if d[0][1] == strX:
      winner = 1
    if d[0][1] == strO:
      winner = 2
  if d[0][2] == d[1][2] == d[2][2]:
    if d[1][2] == strX:
      winner = 1
    if d[1][2] == strO:
      winner = 2
  if d[0][0] == d[1][1] == d[2][2]:
    if d[2][2] == strX:
      winner = 1
    if d[2][2] == strO:
      winner = 2
  if d[2][0] == d[1][1] == d[0][2]:
    if d[0][2] == strX:
      winner = 1
    if d[0][2] == strO:
      winner = 2
  if winner == 1:
    print("X is winner")
    exit()
  if winner == 2:
    print("O is winner")
    exit()
  if HowManyMoved >= 8:
    print('Tie Game')
    exit()
i = 0
while winner == 0:
#if winner == 0 : 
  boxes()
  processX()
  output()
  processO()
  output()
  i=i+1
