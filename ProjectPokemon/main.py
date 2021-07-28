print('20377308,朱睦晨')
try:
    import Pokemon
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
    while True:
        a = input()
        try:
            b = int(a)
            if b <= max and b >= 0 :
                return b-1
            else:
                print('请正确地选择:')
        except:
            print('请正确地选择:')
# 比较速度
def speed_order(P1,P2):
    if P1.speed < P2.speed:
        return [P2,P1]
    else:
        return [P1,P2]

# poke进行操作
def play(poke,another):
    print('''%s的回合！\n你的技能:'''%poke.name)
    for i in range(4):
        print('%d:%s        属性:%s,威力:%d,命中率:%d,PP:%d'
        %(i+1,poke.skills[i].name,poke.skills[i].nature.name,poke.skills[i].atk,poke.skills[i].aim,poke.skills[i].PP))
    print('请选择')
    
    while True:
        try:
            choice = get_input(4)
            d_Hp,af = poke.attack(poke.skills[choice],another)
            break
        except:
            print('PP为0，请选择其他技能')
    print('%s攻击%s ,造成了 %d 点伤害%s' 
    %(poke.name,another.name,d_Hp,af))
def aiplay(poke,another,choice):
    print('''%s的回合！\n你的技能:'''%poke.name)
    for i in range(4):
        print('%d:%s        属性:%s,威力:%d,命中率:%d,PP:%d'
        %(i+1,poke.skills[i].name,poke.skills[i].nature.name,poke.skills[i].atk,poke.skills[i].aim,poke.skills[i].PP))
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
Pokemons_all = Pokemon.Pokemons_all
for i in Pokemons_all.keys():
    print('%d:%s'%(i+1,Pokemons_all[i].name))
# 选择
print('选择游戏模式:\n1:与AI对战\n2：玩家对战')
gamemode = get_input(2)
if gamemode == 1:
    print('玩家1选择精灵')
    c = get_input(6)
    P1 = Pokemons_all[c]
    print('玩家2选择精灵')
    while True:
        d= get_input(6)
        if c == d:
            print('请选择另一个')
        else:
            P2 = Pokemons_all[d]
            break

    while True:
        Player_speed_order = speed_order(P1,P2)
        if P1 == Player_speed_order[0]:
            Show_state(P1,P2)
            play(P1,P2)
            if check_winner(P1,P2):
                break
            Show_state(P1,P2)
            play(P2,P1)
            if check_winner(P1,P2):
                break
        else:
            Show_state(P1,P2)
            play(P2,P1)
            if check_winner(P1,P2):
                break
            Show_state(P1,P2)
            play(P1,P2)
            if check_winner(P1,P2):
                break
else:
    c = rand.randint(0,5)
    P1 = Pokemons_all[c]
    print('AI选择了%s'%P1.name)
    print('玩家选择精灵')
    while True:
        d= get_input(6)
        if c == d:
            print('请选择另一个')
        else:
            P2 = Pokemons_all[d]
            break
    # 回合循环
    while True:
        Player_speed_order = speed_order(P1,P2)
        if P1 == Player_speed_order[0]:
            Show_state(P1,P2)
            aichoice = ai.choose_skill(P1,P2)
            aiplay(P1,P2,aichoice)
            if check_winner(P1,P2):
                break
            Show_state(P1,P2)
            play(P2,P1)
            if check_winner(P1,P2):
                break
        else:
            Show_state(P1,P2)
            play(P2,P1)
            if check_winner(P1,P2):
                break
            Show_state(P1,P2)
            aichoice = ai.choose_skill(P1,P2)
            aiplay(P1,P2,aichoice)
            if check_winner(P1,P2):
                break