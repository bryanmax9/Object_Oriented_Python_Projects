import enemy_factory
import random
import easy_goblin
import easy_ogre
import easy_troll
class BeginnerFactory(enemy_factory.EnemyFactory):
  def create_random_enemy(self):
    nameList = [easy_goblin.EasyGoblin , easy_troll.EasyTroll, easy_ogre.EasyOgre]
    enemy = nameList[random.randint(0,len(nameList)-1)]
    return enemy