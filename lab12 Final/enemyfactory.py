import abc
class EnemyFactory(abc.ABC):
    '''This is the base factory that will be used to create two other factories'''
    @abc.abstractmethod
    def create_random_enemy(self):
        pass
