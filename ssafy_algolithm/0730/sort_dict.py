from operator import itemgetter
people =[
    {'name':'kim4','age':40},
    {'name':'kim1','age':10},
    {'name':'kim5','age':50},
    {'name':'kim3','age':30},
    {'name':'kim7','age':20},
    
]
data =sorted(people,key =itemgetter('name'))

for d in data:
    print(d)