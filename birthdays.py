from datetime import datetime
from collections import defaultdict

# Список днів тижня
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Список користувачів та їхніх днів народження
user_list = [
    {'John': datetime(year=1997, month=12, day=3)},
    {'Alice': datetime(year=1978, month=12, day=4)},
    {'Bob': datetime(year=2000, month=12, day=5)},
    {'Eva': datetime(year=2002, month=12, day=5)},
    {'David': datetime(year=2002, month=12, day=17)},
    {'Sophia': datetime(year=1976, month=12, day=16)},
    {'Oliver': datetime(year=1978, month=12, day=15)},
    {'Lily': datetime(year=2007, month=12, day=14)},
    {'Ethan': datetime(year=2007, month=12, day=10)},
    {'Emma': datetime(year=2002, month=12, day=14)},
    {'Mia': datetime(year=2002, month=12, day=13)},
    {'Noah': datetime(year=2002, month=12, day=12)},
    {'Ava': datetime(year=2002, month=12, day=11)},
    {'James': datetime(year=2002, month=12, day=9)},
    {'Isabella': datetime(year=2002, month=12, day=9)},
]

def congratulate(users: list):
    birthday_current_week = defaultdict(list)
    birthday_next_week = defaultdict(list)
    start_of_year = datetime(year=datetime.now().year, month=1, day=1)
    while start_of_year.weekday() != 0:
        start_of_year = start_of_year.replace(day=start_of_year.day + 1)

    for employee in users:
        for ind, val in employee.items():
            val = val.replace(year=datetime.now().year)

            birthday_number_of_week = (val - start_of_year).days // 7

            if birthday_number_of_week == (datetime.now() - start_of_year).days // 7:
                if val.weekday() <= 4:
                    birthday_current_week[val.weekday()].append(ind)
                else:
                    birthday_next_week[0].append(ind)

            if birthday_number_of_week == (datetime.now() - start_of_year).days // 7 + 1:
                birthday_next_week[val.weekday()].append(ind)

    print('\nNext week we will congratulate!:\n')

    for el in sorted(birthday_next_week.items(), key=lambda t: t[0]):
        names_to_congratulate = ', '.join(el[1])
        print(f'{days_of_week[el[0]]}: {names_to_congratulate}')


congratulate(user_list)