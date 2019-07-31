from human_player import HumanPlayer

from board import Board

brd = Board()
p1 = HumanPlayer('X','Chris')
p2 = HumanPlayer('O','Stacy')

while True:
    
    print(brd)
    m = p1.get_move(brd)
    brd.make_move(m,p1.get_token())
    
    status = brd.get_status()
    if status!='Play':
        print(brd)
        print('Winner',status)
        break
    
    print(brd)
    m = p2.get_move(brd)
    brd.make_move(m,p2.get_token())

    status = brd.get_status()
    if status!='Play':
        print(brd)
        print('Winner',status)
        break