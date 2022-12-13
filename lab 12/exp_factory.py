import enemy_factory
import random
import goblin
import ogre
import troll 
class ExpertFactory(enemy_factory.EnemyFactory):
  def create_random_enemy(self):
    nameList = [goblin.Goblin,ogre.Ogre, troll.Troll]
    enemy = nameList[random.randint(0,len(nameList)-1)]
    return enemy