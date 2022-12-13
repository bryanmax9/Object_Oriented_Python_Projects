import abc
class Entity (abc.ABC):
    '''This is the abstract class that will be used to create other classes more actual
    application of these modules and also redefinition of these modules.'''
    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    @property
    def name(self):
        '''this is the getter of name so it will return
        the name on request'''
        return self._name

    @property
    def hp(self):
        '''this is the getter of hp it will return the hp that class
        has at that time
        '''
        return self._hp
 
    def take_damage (self, dmg):
        '''This method is responsible for the damage that will be given to this
        class when needed and requested'''
        if (self._hp - dmg) < 0:
            self._hp = 0
        else:
            self._hp = self._hp - dmg
    def heal (self):
        '''This method will heal the class to full health meaning health will be maxed
        out on request'''
        self._hp = self._max_hp
    def __str__(self):
        '''This the string method of class and how the class will print itself out on request'''
        form = self._name+"\n"
        form += "HP:"+str(self._hp)+"/"+str(self._max_hp)
        return form

    @abc.abstractmethod
    def attack(self,entity):
        '''This is the attack method that will be redefined in other classes due to
        differences in use. It will deal damage to another class'''
        pass
