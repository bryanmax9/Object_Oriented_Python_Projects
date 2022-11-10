import entity
import random
class Enemy(entity.Entity):
    def __init__(self):
        nameList = ["Goblin" , "Troll" , "Ghoul" , "Skeleton" , "Kobold" , "Mike Wazowski", "Sulley"]
        _name = nameList[random.randint(0,len(nameList)-1)]
        _hp = random.randint(4,8)
        super().__init__(_name,_hp)
    def attack(self,entity):
        damage = random.randint(1,4)
        entity.take_damage(damage)
        return self.name + " attacks a " + entity.name + " for " + str(damage) + " damage."
