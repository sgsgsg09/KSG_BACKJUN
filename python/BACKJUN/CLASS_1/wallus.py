import random

def pick_fruit():
    if random.randint(1,10) > 2:   # 80% 확률로 새 과일 보충
        return {
            '사과': random.randint(0,10),
            '바나나': random.randint(0,10),
            '레몬': random.randint(0,10),
        }
    else:
        return None

def make_juice(fruit, count):
    if fruit == '사과':
        return [('사과주스', count/4)]
    elif fruit == '바나나':
        return [('바나나스무디',count/2)]
    elif fruit == '레몬':
        return [('레모네이드',count/1)]
    else:
        return []
bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
print(bottles)