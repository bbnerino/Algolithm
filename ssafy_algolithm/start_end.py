def start_end(words):
    result = []
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            result.append(i)
    return result
    
    print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))