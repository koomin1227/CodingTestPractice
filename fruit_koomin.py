STRAWBERRY_AND_APPLE_DAY = [1,5]
WATERMELON_AND_PEAR_DAY = [3, 7]
SPRING = [3,4,5]
SUMMER = [6,7,8]
FALL = [9,10,11]
WINTER = [1,2,12]
SPRING_SUMMER_FRUIT = ['딸기', '수박']
FALL_WINTER_FRUIT = ['사과', '배']

def get_first_digit(num):
    num = list(str(num))
    return int(num.pop())

def get_fruit_with_day(season_fruits, day):
    if get_first_digit(day) in STRAWBERRY_AND_APPLE_DAY:
        return season_fruits[0]
    elif get_first_digit(day) in WATERMELON_AND_PEAR_DAY:
        return season_fruits[1]

def get_fruit(month, user_count, day):
    if month in SPRING or month in SUMMER:
        return get_fruit_day(SPRING_SUMMER_FRUIT, day)
    elif month in FALL or month in WINTER:
        return get_fruit_day(FALL_WINTER_FRUIT, day)
    else: 
        return None

def calculate_strawberry_count(user_count):
    count = user_count * 5
    return count

def calculate_apple_count(user_count):
    count = user_count
    return count

def calculate_watermelon_count(user_count):
    count = user_count // 10
    if user_count % 10 != 0:
        count += 1
    return count

def calculate_pear_count(user_count):
    count = user_count // 2
    if user_count % 2 != 0:
        count += 1
    return count

def get_fruit_count(fruit, user_count):
    if fruit == '딸기':
        return calculate_strawberry_count(user_count)
    elif fruit == '수박':
        return calculate_watermelon_count(user_count)
    elif fruit == '사과':
        return calculate_apple_count(user_count)
    elif fruit == '배':
        return calculate_pear_count(user_count)
    else: 
        return 3


month, user_count = map(int, input().split())

for day in range(1,31):
    fruit = get_fruit(month, user_count, day)
    if fruit == None:
        print(day, 'no')
    else:
        fruit_count = get_fruit_count(fruit, user_count)
        print(day, fruit, fruit_count)


# 