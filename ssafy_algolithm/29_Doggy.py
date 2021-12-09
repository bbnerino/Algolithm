class Doggy:
    nums_of_dogs = 0 
    birth_of_dogs = 0

    def __init__(self,name,jong):
        
        self.name = name
        self.jong = jong
        Doggy.birth_of_dogs +=1
        Doggy.nums_of_dogs +=1

    def __del__(self):
        Doggy.nums_of_dogs -=1   

    def bark(self):
        print("왈왈")

    @classmethod
    def get_status(self):
        
        print(f"Birth:{Doggy.birth_of_dogs}, Current:{Doggy.nums_of_dogs}")
        
d1 = Doggy('초코', '푸들')
d2 = Doggy('꽁이', '말티즈')
d3 = Doggy('별이', '시츄')

d1.bark() #=> 왈왈!
d2.bark() #=> 왈왈!
d3.bark() #=> 왈왈!
Doggy.get_status() 
del(d1)
Doggy.get_status() #=> Birth: 3, Current: 3