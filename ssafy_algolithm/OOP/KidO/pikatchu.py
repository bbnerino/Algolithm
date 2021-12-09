from Encyclopedia.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25
    def __init__(self, name):
        super().__init__(name)
        self.age = 1
        self.lv = 1
        self.skill = '전기 충격'

    def walk(self):
        return '뚜벅뚜벅'

class Metamong(Pokemon):
    no = 132

    def __init__(self, name):
        super().__init__(name)
        self.age = 1
        self.lv = 1

    def attack(self):
        return '변신'

    def eat(self):
        return '냠냠'

class Child(Pikatchu, Metamong):
    pass

class Brother(Metamong, Pikatchu):
    def eat(self):
        return '우걱우걱'

c = Child('피카츄?')
# print(c.walk())
# print(c.eat())
# print(c.attack())
# print(c.no)

d = Brother('메타몽?')
print(d.no)
print(d.eat())


