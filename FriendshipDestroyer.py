GameIO = 1
m=16 
n=16
Chess_List = [[0 for i in range(m)] for j in range(n)]

def ShowList():
    """画棋盘"""
    for i in range(m):
        for j in range(n):
            print(Chess_List[i][j],end="")
        print ("")

def GetChess(Playernum,i,j):
    "棋手编号，行，列"
    if Chess_List[i][j] != 0:
        print("?这是二维棋盘！")
        i=int(input("你要下在第几行？"))-1
        j=int(input("你要下在第几列？"))-1
        GetChess(Player,i,j)
    else:
        Chess_List[i][j]= int(Playernum)

def CheckWinner(Playernum):
    "某棋手赢了没？"
    pptty=1
    for i in range(16):
        for j in range(16):
            if Chess_List[i][j] == Playernum:
                "他在这里下了一步"
                jl = j-4
                idown = i+4
                jr = j+4
                if idown >= m or jr >=n :
                    continue
                else: 
                    r = j+1
                    "→"
                    if Chess_List[i][r] == Playernum:
                        for p in range(3):
                            r=r+1
                            if p ==1:
                                print('玩家',Playernum,'接近胜利！')
                            if p ==2:
                                print('玩家',Playernum,'赢了！')
                                pptty = 0
                            if Chess_List[i][r] != Playernum:
                                break
                    d = i+1 
                    "↓"
                    if Chess_List[d][j] == Playernum:
                        for p in range(3):
                            d = d+1
                            if p ==1:
                                print('玩家',Playernum,'接近胜利！')
                            if p ==2:
                                print('玩家',Playernum,'赢了！')
                                pptty = 0
                            if Chess_List[d][j] != Playernum:
                                break
                    rd = j+1
                    dr = i+1
                    "↘"
                    if Chess_List[dr][rd] == Playernum:
                        for p in range(3):
                            rd = rd+1
                            dr = dr+1
                            if p ==1:
                                print('玩家',Playernum,'接近胜利！')
                            if p ==2:
                                print('玩家',Playernum,'赢了！')
                                pptty = 0
                            if Chess_List[dr][rd] != Playernum:
                                break
                    if jl>= 0:
                        ld = j-1
                        dl = i+1
                        "↙"
                        if Chess_List[dl][ld] == Playernum:
                            for p in range(3):
                                ld = ld-1
                                dl = dl+1
                                if p ==1:
                                    print('玩家',Playernum,'接近胜利！')
                                if p ==2:
                                    print('玩家',Playernum,'赢了！')
                                    pptty = 0
                                if Chess_List[dl][ld] != Playernum:
                                    break
    return pptty

while GameIO:
    for Playernum in range(3):
        Player = Playernum + 1
        i=int(input("你要下在第几行？"))-1
        j=int(input("你要下在第几列？"))-1
        GetChess(Player,i,j)
        GameIO = CheckWinner(Player)
        if GameIO == 0:
            break
        ShowList()
input("写点啥退出吧>>")    
