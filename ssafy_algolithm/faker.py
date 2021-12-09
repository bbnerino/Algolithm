from faker import Faker 
fake = Faker() # 2. Faker는 class, fake는 Faker의 인스턴스이다
fake.name()  # 3. name()은 fake의 method이다.

fake = Faker()
fake.name()
# -> 영문

fake_ko = Faker('ko_KR')
print(fake_ko.name())
# -> 서경수

# class Faker():
# 	def __(a)__((b),(c)):
# 		pass
# a= init
# b= self
# c= locale= "en_US"
from faker import Faker
fake = Faker('ko_KR')

Faker.seed(4321)
print(fake.name()) # 이도윤
fake2 = Faker('ko_KR')
print(fake2.name()) # 이지후

Faker.seed(4321)
print(fake.name()) # 이도윤
fake2 = Faker('ko_KR')
print(fake2.name()) # 이지후

Faker.seed(4321)
print(fake.name()) # 이도윤
fake2 = Faker('ko_KR')
print(fake2.name()) # 이지후

fake =Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name()) #이도윤

fake2 = Faker('ko_KR')
print(fake2.name()) # 최,김,이,박....