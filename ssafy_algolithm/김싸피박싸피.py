import random
class ClassHelper:
    def __init__(self,listperson) :
        self.persons = listperson
        pass
    def pick(self,count):

        
        print(random.sample(self.persons,count))
        
    def match_pair(self): 
        random.shuffle(self.persons)
        if len(self.persons)%2 == 0:
            i=0
            while i != len(self.persons): 
                print([self.persons[i],self.persons[i+1]],end=",")
                i += 2



        else: # 홀수일때
            print([self.persons[0],self.persons[1]])
            i=0
            while i != len(self.persons)-3: 
                print([self.persons[i],self.persons[i+1]],end=",")
                i += 2
            print([self.persons[-3],self.persons[-2],self.persons[-1]])

    
    
            



ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피','임싸피','흠싸피'])

ch.pick(1) #=> ['이싸피']
ch.pick(1) #=> ['김싸피']
ch.pick(2) #=> ['김싸피', '박싸피']
ch.pick(3) #=> ['김싸피', '조싸피', '정싸피']
ch.pick(4) #=> ['박싸피', '이싸피', '김싸피', '정싸피']

ch.match_pair() #=> [['조싸피', '이싸피'], ['김싸피', '정싸피', '박싸피']]