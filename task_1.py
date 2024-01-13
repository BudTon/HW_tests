def identify_zodiac_sign(day, month):
    signs = {"март": (21, "Рыбы", "Овен"), "апрель": (21, "Овен", "Телец"), "май": (22, "Телец", "Близнецы"),
         "июнь": (22, "Близнецы", "Рак"), "июль": (23, "Рак", "Лев"), "август": (24, "Лев", "Дева"),
         "сентябрь": (24, "Дева", "Весы"), "октябрь": (24, "Весы", "Скорпион"),
         "ноябрь": (23, "Скорпион", "Стрелец"), "декабрь": (23, "Стрелец", "Козерог"),
         "январь": (21, "Козерог", "Водолей"), "февраль": (20, "Водолей", "Рыбы")}
    # day, month = int(input("Введите день - ")), input("Введите месяц - ")
    return signs[month][2] if (day >= signs[month][0]) else signs[month][1]

def perimeter_and_area_square(a):
    perimeter = a * 4  # Расчёт периметра
    area = a * a  # Расчёт площади

    # print('Периметр: ', perimeter)
    # print('Площадь: ', area)

    return perimeter, area


def financial_calculator(salary: int, percent_mortgage: int, percent_life: int) -> int:
    # salary = 100000  # Заработная плата
    # percent_mortgage = 30  # Ипотека
    # percent_life = 50  # На жизнь
    mortgage = (salary*percent_mortgage/100)*12
    result = (salary-mortgage/12-salary*percent_life/100)*12
    # print('Ипотека:', mortgage)
    # print('Накопления:', result)
    return mortgage, result


if __name__ == "__main__":
    mortgage, result = financial_calculator(220000, 30, 50)
    print('Ипотека:', mortgage, f'\n''Накопления:', result)

    perimeter, area = perimeter_and_area_square(7)
    print('Периметр: ', perimeter, f'\n''Площадь: ', area)

    day, month = 10, 'май'
    # day, month = int(input("Введите день - ")), input("Введите месяц - ")
    print(identify_zodiac_sign(day, month))


