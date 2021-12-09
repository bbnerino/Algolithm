def count_blood(blood_types):
    result ={}
    for blood in blood_types:
        result[blood] =result.get(blood,0)+1
        # key 찾았는데 없으면 none 대신 0을 반환
    print(result)
count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
])