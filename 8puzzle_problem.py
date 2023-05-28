class node(object):

    def __init__(self,board,parent=None,level=0):

        self.board=board
        self.pos=self.getpos()
        self.parent=parent
        self.level=level

    def getpos(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]==0:
                    return (i,j)
    
    def check_pos(self):
        if self.pos in [(0,0),(0,2),(2,0),(2,2)]:
            return 2
        elif self.pos==(1,1):
            return 4
        else:
            return 3
    
    def find_possible_pairs(self):
        if self.check_pos()==2:
            if self.pos==(2,2):
                return (1,2),(2,1)
            elif self.pos==(2,0):
                return (2,1),(1,0)
            elif self.pos==(0,0):
                return (1,0),(0,1)
            else:
                return (0,1),(1,2)
        
        elif self.check_pos()==4:
            return (0,1),(1,0),(1,2),(2,1)
        
        else:
            if self.pos==(0,1):
                return (0,0),(0,2),(1,1)
            elif self.pos==(1,0):
                return (0,0),(1,1),(2,0)
            elif self.pos==(2,1):
                return (2,0),(2,2),(1,1)
            else:
                return (0,2),(2,2),(1,1)

def move(b1,pairs,x,poss):
    b1[pairs[x][0]][pairs[x][1]],b1[poss[0]][poss[1]]=b1[poss[0]][poss[1]],b1[pairs[x][0]][pairs[x][1]]

if __name__=='__main__':
    m=node([[3,1,9],
            [5,6,7],
            [8,2,0]])

    goal=[[3,9,7],
        [6,1,2],
        [5,0,8]]
    q=[m]
    max_level=10
    while q:
        cur=q.pop(0)
        if cur.board==goal:
            print('found\n')
            break
        if cur.level>max_level:
            raise Exception(f'solution not found within the given level : {max_level}')
        #first find the possible pairs from the current node
        if cur.check_pos()==2:
            #create two boards
            poss=cur.pos
            pairs=cur.find_possible_pairs()
            b1=[row[:] for row in cur.board]
            move(b1,pairs,0,poss)
            n1=node(b1,cur,cur.level+1)
            b2=[row[:] for row in cur.board]
            move(b2,pairs,1,poss)
            n2=node(b2,cur,cur.level+1)
            q.extend([n1,n2])
        
        if cur.check_pos()==3:
            #create 3 boards
            poss=cur.pos
            pairs=cur.find_possible_pairs()

            b1=[row[:] for row in cur.board]
            move(b1,pairs,0,poss)
            n1=node(b1,cur,cur.level+1)
            b2=[row[:] for row in cur.board]
            move(b2,pairs,1,poss)
            n2=node(b2,cur,cur.level+1)
            b3=[row[:] for row in cur.board]
            move(b3,pairs,2,poss)
            n3=node(b3,cur,cur.level+1)
            q.extend([n1,n2,n3])
            
        
        if cur.check_pos()==4:
            #create 4 boards
            poss=cur.pos
            pairs=cur.find_possible_pairs()
            b1=[row[:] for row in cur.board]
            move(b1,pairs,0,poss)
            n1=node(b1,cur,cur.level+1)
            b2=[row[:] for row in cur.board]
            move(b2,pairs,1,poss)
            n2=node(b2,cur,cur.level+1)
            b3=[row[:] for row in cur.board]
            move(b3,pairs,2,poss)
            n3=node(b3,cur,cur.level+1)
            b4=[row[:] for row in cur.board]
            move(b4,pairs,3,poss)
            n4=node(b4,cur,cur.level+1)
            q.extend([n1,n2,n3,n4])

    vi=[]
    a=cur
    while a:
        vi.append(a.board)
        a=a.parent

    for i in vi[::-1]:
        for j in i:
            print(*j)
        print()
    print(f'solution found at level {cur.level}')
        
	