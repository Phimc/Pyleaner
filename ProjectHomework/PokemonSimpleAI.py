import Pokemon as P

def choose_skill(Poke,another):
    choice = 0
    attack_Hp_Max = 0
    for i in range(len(Poke.skills)):
        skill = Poke.skills[i]
        plus,affect = Poke.find_plus_expect(skill,another)
        attack_Hp = ((2*Poke.level+10)/250*(Poke.atk/another.df)*skill.atk+2)*plus
        if attack_Hp < 1:
            attack_Hp =1
        else:
            attack_Hp = int(attack_Hp)
        
        if attack_Hp>attack_Hp_Max:
            attack_Hp_Max = attack_Hp
            choice = i
    return choice
