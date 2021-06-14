print('20377308,Phmc')
try:
    import Pokemon
    from Pokemon import Pokemons_all
    import PokemonSimpleAI as ai
    import numpy.random as rand
    print('载入成功!')
except:
    print('缺失文件，游戏无法开始')

# 状态
def Show_state(A,B):
    print('''-----------------------------------------\n%s的HP:%d/%d\n%s的HP:%d/%d'''
    %(A.name,A.Hp,A.MaxHp,B.name,B.Hp,B.MaxHp))
# 检测输入
def get_input(max):
    a = input()
    while True:
        try:
            b = int(a)
            if b <= max and b >= 0 :
                return b-1
            else:
                print('请正确地选择:')
        except:
            print('请正确地选择:')
# poke进行操作
def play(poke,another):
    print('''%s的回合！\n你的技能:'''%poke.name)
    for i in range(4):
        print('%d:%s        属性:%s,威力:%d,命中率:%d'
        %(i+1,poke.skills[i].name,poke.skills[i].nature.name,poke.skills[i].atk,poke.skills[i].aim))
    print('请选择')
    choice = get_input(4)
    d_Hp,af = poke.attack(poke.skills[choice],another)
    print('%s攻击%s ,造成了 %d 点伤害%s' 
    %(poke.name,another.name,d_Hp,af))
def aiplay(poke,another,choice):
    print('''%s的回合！\n你的技能:'''%poke.name)
    for i in range(4):
        print('%d:%s        属性:%s,威力:%d,命中率:%d'
        %(i+1,poke.skills[i].name,poke.skills[i].nature.name,poke.skills[i].atk,poke.skills[i].aim))
    print('请选择')
    print(choice)
    d_Hp,af = poke.attack(poke.skills[choice],another)
    print('%s攻击%s ,造成了 %d 点伤害%s' 
    %(poke.name,another.name,d_Hp,af))
# 胜负判定
def check_winner(A,B):
    if A.Hp == 0:
        print('%s获胜!'%B.name)
        return True
    elif B.Hp == 0:
        print('%s获胜'%A.name)
        return True
    else:
        return False 

# 游戏
for i in Pokemons_all.keys():
    print('%d:%s'%(i+1,Pokemons_all[i].name))
# 选择
print('选择游戏模式:\n1:与AI对战\n2：玩家对战')
gamemode = get_input(2)
if gamemode == 1:
    print('玩家1选择精灵')
    c = get_input(5)
    P1 = Pokemons_all[c]
    print('玩家2选择精灵')
    while True:
        d= get_input(5)
        if c == d:
            print('请选择另一个')
        else:
            P2 = Pokemons_all[d]
            break

    while True:
        Show_state(P1,P2)
        play(P1,P2)
        if check_winner(P1,P2):
            break
        Show_state(P1,P2)
        play(P2,P1)
        if check_winner(P1,P2):
            break
else:
    c = rand.randint(0,4)
    P1 = Pokemons_all[c]
    print('玩家选择精灵')
    while True:
        d= get_input(5)
        if c == d:
            print('请选择另一个')
        else:
            P2 = Pokemons_all[d]
            break

    while True:
        Show_state(P1,P2)
        aichoice = ai.choose_skill(P1,P2)
        aiplay(P1,P2,aichoice)
        if check_winner(P1,P2):
            break
        Show_state(P1,P2)
        play(P2,P1)
        if check_winner(P1,P2):
            break