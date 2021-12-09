def get_dict_avg(test):
    score = 0
    for key, value in test.items():
        score += value
    print(score/len(test))

## sum(socres.values()/ len(scores))
    
get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83
})