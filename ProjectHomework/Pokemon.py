# Store Information of Pokemons
import numpy.random as rand

# 属性
class Nature:
    def __init__(self,name) :
        '''精灵、技能属性\nname=名字'''
        self.name = name


normal = Nature('一般')
act = Nature('格斗')
fire = Nature('火')
ice = Nature('冰')
electric = Nature('电')

plus_dict = {}
plus_dict[normal]   = {normal:1,  act:1,  fire:1,  ice:1,  electric:1}
plus_dict[act]      = {normal:2,  act:1,  fire:1,  ice:0.5,electric:1}
plus_dict[fire]     = {normal:1,  act:1,  fire:1,  ice:2,  electric:1}
plus_dict[ice]      = {normal:1,  act:1,  fire:1,  ice:0.5,electric:2}
plus_dict[electric] = {normal:1,  act:2,  fire:1,  ice:0.5,electric:1}
af = {0.5:'，效果不佳。',1:'。',2:'，效果拔群！'}

# 技能
class Skill:
    def __init__(self,nature,atk,aim,PP,name):
        '''技能\nnature=属性，atk=威力，aim=命中率，PP=最大使用次数，name=名字'''
        self.PP = PP
        self.nature = nature
        self.atk = atk
        self.aim = aim
        self.name = name


# 神奇宝贝
class Pokemon:
    def __init__(self,skills,nature,name,Hp,atk,df,speed):
        
        self.skills = skills
        self.nature = nature
        self.name = name
        self.MaxHp = Hp
        self.Hp = Hp
        self.level = 50
        self.atk = atk
        self.df = df      
        self.speed=speed
    # 计算加成
    def find_plus(self,skill,poke):
        nature_plus = plus_dict[skill.nature][poke.nature]
        if self.nature == skill.nature:
            nature_correspond = 1.5
        else:
            nature_correspond = 1
        if rand.rand() > 0.95:
            strategic_plus = 2
        else:
            strategic_plus = 1
        return [nature_correspond*nature_plus*strategic_plus,nature_plus]
    # 计算伤害期望
    def find_plus_expect(self,skill,poke):
        nature_plus = plus_dict[skill.nature][poke.nature]
        if self.nature == skill.nature:
            nature_correspond = 1.5
        else:
            nature_correspond = 1
        strategic_plus = 1.1
        return [nature_correspond*nature_plus*strategic_plus,nature_plus]
    # 攻击
    def attack(self,skill,poke):
        if skill.PP > 0:
            skill.PP -= 1
        else:
            raise Exception
        plus,affect = self.find_plus(skill,poke)
        attack_Hp = ((2*self.level+10)/250*(self.atk/poke.df)*skill.atk+2)*plus
        if attack_Hp < 1:
            attack_Hp =1
        else:
            attack_Hp = int(attack_Hp)
        poke.Hp -= attack_Hp
        if poke.Hp < 0:
            poke.Hp =0
        k = af[affect]
        return [attack_Hp,k]


#******#
thunder_shock = Skill(electric,40,100,30,'电击')
nuzzle = Skill(electric,20,100,20,'蹭蹭脸颊')
discharge = Skill(electric,80,100,15,'放电')
feint = Skill(normal,30,100,10,'佯攻')
#******#
pay_day = Skill(normal,40,100,20,'聚宝功')
snore = Skill(normal,50,100,15,'打鼾')
fake_out = Skill(normal,40,100,10,'击掌奇袭')
slash = Skill(normal,90,100,15,'劈开')
#******#
scratch = Skill(normal,40,100,35,'抓')
ember = Skill(fire,40,100,25,'火花')
fire_punch = Skill(fire,75,100,15,'火焰拳')
inferno = Skill(fire,100,50,5,'炼狱')
#******#
powder_snow = Skill(ice,40,100,25,'细雪')
blizzard = Skill(ice,110,70,5,'暴风雪')
ice_punch = Skill(ice,75,100,15,'冰冻拳')
crunch = Skill(ice,80,100,15,'咬碎')
#******#
pound = Skill(normal,40,100,35,'拍击')
tackle = Skill(normal,40,100,35,'撞击')
karate_chop = Skill(act,50,100,25,'空手劈')
headbutt = Skill(normal,70,100,15,'头锤')
#******#
fury_swipes = Skill(act,18,80,15,'乱抓')
thrash = Skill(act,120,100,10,'大闹一番')
low_kick = Skill(act,70,100,20,'踢倒')
brick_break = Skill(act,75,100,15,'劈瓦')


Pikachu = Pokemon([thunder_shock,nuzzle,discharge,feint],electric,'皮卡丘',120,112,88,90)
Meowth = Pokemon([pay_day,snore,fake_out,slash],normal,'喵喵',130,105,67,91)
Charmander = Pokemon([scratch,fire_punch,inferno,ember],fire,'小火龙',140,110,100,63)
Snorunt = Pokemon([powder_snow,blizzard,ice_punch,crunch],normal,'雪童子',150,90,100,50)
Skitty = Pokemon([pound,karate_chop,tackle,headbutt],normal,'向尾喵',150,98,105,49)
Mankey = Pokemon([fury_swipes,thrash,low_kick,brick_break],act,'猴怪',140,130,80,92)

Pokemons_all = {
0:Pikachu,
1:Meowth,
2:Charmander,
3:Snorunt,
4:Skitty,
5:Mankey
}