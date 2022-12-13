import enemyfactory
import Troll
import Ogre
import Goblin
import random
class ExpertFactory (enemyfactory.EnemyFactory):
    '''This is the harder factory that will generate harder enemies for the user to fight with'''
    def create_random_enemy(self):
        '''This is how the enemies will be generated
        Args:
        self: How to enter objects for the class
        Return:
        Enenmies (classes): These are the enemies to be returned to the game for the user
        to fight with'''
        randomEnemy = random.randint(1,3)
        if randomEnemy == 1:
            return Troll.Troll()
        elif randomEnemy == 2:
            return Ogre.Ogre()
        elif randomEnemy == 3:
            return Goblin.Goblin()
