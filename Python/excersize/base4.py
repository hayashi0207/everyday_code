# print(dict_a)
class CharacterAlreadyExistException(Exception):
    pass

class AllCharacters:

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls,name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターは既に登録されています。')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls,name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:

    def __init__(self,name,hp,offense,defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self,enemy,critical_point=1):
        if self.hp <=0:
            print('キャラクターは既に死んでします')
            return
        attack_point = self.offense - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)  

    def critical_hit(self,enemy):
        self.attack(enemy,2)

character_a = Character('A',10,5,3)
character_b = Character('B',8,6,2)

print(character_b.hp)
character_a.attack(character_b)
character_a.critical_hit(character_b)
print(character_b.hp)
character_a.attack(character_b)
