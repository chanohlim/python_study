import random
import os

quiz = {'포르쉐':'911',
        '현대':'아반떼',
        '벤츠':'S-클래스',
        '람보르기니':'아벤타도르',
        '기아':'K5',
        '페라리':'라페라리',
        '테슬라':'모델 S',
        'BMW' : '520i',
        '아우디' : 'R8',
        '쌍용' : '렉스턴'
        }

brand = list(quiz.keys())
car = list(quiz.values())

try:
    os.makedirs('/Users/chanlim/Desktop/ /code/python_study/quiz')
    os.makedirs('/Users/chanlim/Desktop/ /code/python_study/answer')
except:
    pass

for i in range(10):
    f = open(f'/Users/chanlim/Desktop/ /code/python_study/quiz/퀴즈 {i+1}번','w')
    ans = open(f'/Users/chanlim/Desktop/ /code/python_study/answer/정답 {i+1}번','w')

    random.shuffle(brand)
    cnt = 1
    for j in brand:
        brand = list(quiz.keys())
        car = list(quiz.values())
        f.write(f'#{cnt}) "{j}" 브랜드인 차를 고르시오.\n\n')
        car.remove(quiz[j])
        random.shuffle(car)
        choice = random.sample(car,3)
        choice = choice + [quiz[j]]
        random.shuffle(choice)
        for k in range(4):
            f.write(f'{k+1}번: {choice[k]}\n')
        f.write('\n\n')

        ans.write(f'{cnt}번: {choice.index(quiz[j]) + 1}\n\n')

        cnt += 1

    f.close()
    ans.close()
