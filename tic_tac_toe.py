def print_board(a):
    print(f'   {a[1]}  |     {a[2]}     |  {a[3]} ')
    print('--------------------------')
    print(f'   {a[4]}  |     {a[5]}     |  {a[6]} ')
    print('--------------------------')
    print(f'   {a[7]}  |     {a[8]}     |  {a[9]} ')



def print_instruction():
    print('\n ----------------Welcome To Tic Tac Toe----------------\n\n')
    print_board(pos)
    print('\n')
    player[0]=input('Enter Player1 name : ')
    player[1]=input('Enter Player2 name : ')
    print('\n-------------Instructions-------------\n')
    print('-->',player[0],'you will using X')
    print('-->',player[1],'you will using O')
    print('Turn Start From ',player[0])
    ######Board positons #############
    print("Positions are like :- ")
    print("   1   |   2   |   3    ")
    print('----------------------')
    print("   4   |   5   |   6    ")
    print('----------------------')
    print("   7   |   8   |   9    ")
    print('--> Press S to start the game')
    flag=input().lower()
    return flag

    
def startgame():
    turn=0
    for i in range(9):
        if turn%2==0:
            print('\n this is your turn ', player[0])
            p=int(input('Enter the position : '))
            v='X'
            pos[p]=v
            print_board(pos)
            winner= checkwin(v)
            if winner is 'nobody':
                turn =1
                continue
            else:
                print(f'congratulations {player[0]} wins')
                break
        else:
            print('\n this is your turn ', player[1])
            p=int(input('Enter the position : '))
            v='O'
            pos[p]=v
            print_board(pos)
            winner= checkwin(v)
            if winner is 'nobody':
                turn =0
                continue
            else:
                print(f'congratulations {player[1]} wins')
                break
    else:
        print('tie') 

def checkwin(v):

    for i in wining_conditions:
        if (pos[i[0]],pos[i[1]],pos[i[2]])==(v,v,v):
            winner = player[0]
            break
        elif(pos[i[0]],pos[i[1]],pos[i[2]])==(v,v,v):
                winner = player[1]
                break
        else:
            winner='nobody'
    return winner    
            
# #main code 
pos=['','','','','','','','','','']

player=['','']

wining_conditions=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
# print_instruction()

flag= print_instruction()

if flag =='s':
    startgame()

else:
    print('invalid entry')