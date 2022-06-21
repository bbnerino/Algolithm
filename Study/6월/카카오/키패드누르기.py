numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

#147은 왼손 , 369는 오른손
#2580은 현재 키패드에의 위치에서 더 가까운 손가락
#거리가 같다면 주손을 사용


def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]
    keyboard = [[3,1],
                [0,0],[0,1],[0,2],
                [1,0],[1,1],[1,2],
                [2,0],[2,1],[2,2],
                [3,0],[3,2]]
    last_left = 10
    last_right = 11
    for i in numbers:
        if i in left:
            answer+='L'
            last_left = i
        elif i in right:
            answer+='R'
            last_right = i
        else:
            length_left = abs(keyboard[i][0] - keyboard[last_left][0]) + abs(keyboard[i][1] - keyboard[last_left][1])
            length_right = abs(keyboard[i][0] - keyboard[last_right][0]) + abs(keyboard[i][1] - keyboard[last_right][1])
            if length_left > length_right:
                last_right = i
                answer +='R'
            elif length_left < length_right:
                last_left = i
                answer +='L'
            elif length_left == length_right:
                if hand=='right':
                    last_right = i
                    answer += 'R'
                else:
                    last_left = i
                    answer += 'L'
    print(answer)
    return answer

solution(numbers,hand)