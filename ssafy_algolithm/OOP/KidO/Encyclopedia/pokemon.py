class Pokemon:
    name = 'missing no'
    population = 0
    age = 0
    lv = 0

    def __init__(self, name):
        Pokemon.population += 1
        self.name = name
        self.skill = '몸통 박치기'
        
        print(f'{name} {name}')

    def attack(self):
        return self.skill        

    @classmethod # 클래스로만 접근하자.
    def info(cls):
        return cls.population

    @staticmethod # 클래스로만 접근하자.
    def poke():
        return '푸키먼..'

# a = Pokemon('피카츄')
# b = Pokemon('메타몽')
# print(a.attack(), b.attack())

# print(a.info()) # 인스턴스는 클래스 메서드 호출 가능하다.
# print(a.poke()) # 인스턴스는 스태틱 메서드 호출 가능하다.
# 호출 가능하지만 그렇게 사용하지 않을 것이다.