# Store Information of Pokemons
# 倍率
import numpy.random as rand

# 属性
class Nature:
    def __init__(self,name) :
        self.name = name
normal = Nature('normal')
act = Nature('act')
fire = Nature('fire')
ice = Nature('ice')
electric = Nature('electric')

plus_dict = {}
plus_dict[normal]   = {normal:1,  act:1,  fire:1,  ice:1,  electric:1}
plus_dict[act]      = {normal:2,  act:1,  fire:1,  ice:0.5,electric:1}
plus_dict[fire]     = {normal:1,  act:1,  fire:1,  ice:2,  electric:1}
plus_dict[ice]      = {normal:1,  act:1,  fire:1,  ice:0.5,electric:1}
plus_dict[electric] = {normal:1,  act:2,  fire:1,  ice:1,  electric:1}
af = {0.5:'，效果不佳。',1:'。',2:'，效果拔群！'}

# 技能
class Skill:
    def __init__(self,nature,atk,aim,PP,name):
        self.PP = PP
        self.nature = nature
        self.atk = atk
        self.aim = aim
        self.name = name

thunder_shock = Skill(electric,40,100,30,'thunder shock')
nuzzle = Skill(electric,20,100,20,'nuzzle')
slam = Skill(normal,80,75,20,'slam')
feint = Skill(normal,30,100,10,'feint')
pay_day = Skill(normal,40,100,20,'pay_day')
snore = Skill(normal,50,100,15,'snore')
icy_wind = Skill(ice,55,95,15,'ice wind')
thunderbolt = Skill(electric,90,100,15,'thunderbollt')
scratch = Skill(normal,40,100,35,'scratch')
ember = Skill(fire,40,100,25,'ember')
fire_punch = Skill(fire,75,100,15,'fire_punch')
inferno = Skill(fire,100,50,5,'inferno')
powder_snow = Skill(ice,40,100,25,'powder_snow')
blizzard = Skill(ice,110,70,5,'blizzard')
ice_punch = Skill(ice,75,100,15,'ice_punch')
pound = Skill(normal,40,100,35,'pound')
tackle = Skill(normal,40,100,35,'tackle')
karate_chop = Skill(act,50,100,25,'karate chop')
headbutt = Skill(normal,70,100,15,'headbutt')

# 神奇宝贝
class Pokemon:
    def __init__(self,skills,nature,name):
        self.skills = skills
        self.nature = nature
        self.MaxHp = 50
        self.Hp = 50
        self.level = 20
        self.atk = 45
        self.df = 45
        self.name = name

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
    
    def find_plus_expect(self,skill,poke):
        nature_plus = plus_dict[skill.nature][poke.nature]
        if self.nature == skill.nature:
            nature_correspond = 1.5
        else:
            nature_correspond = 1
        strategic_plus = 1.1
        return [nature_correspond*nature_plus*strategic_plus,nature_plus]

    def attack(self,skill,poke):
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

Pikachu = Pokemon([slam,thunder_shock,nuzzle,feint],electric,'Pikachu')
Meowth = Pokemon([pay_day,snore,icy_wind,thunderbolt],normal,'Meowth')
Charmander = Pokemon([scratch,fire_punch,inferno,ember],fire,'Charmander')
Snorunt = Pokemon([powder_snow,blizzard,ice_punch,icy_wind],normal,'Snorunt')
Skitty = Pokemon([pound,karate_chop,tackle,headbutt],normal,'Skitty')

Pokemons_all = {
0:Pikachu,
1:Meowth,
2:Charmander,
3:Snorunt,
4:Skitty
}
