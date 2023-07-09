# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

city = input('City: ')
def check_country(city):
    dict_country = {
        'BY': ['minsk', 'grodno', 'brest'],
        'RU': ['moskva', 'piter', 'smolensk'],
    }

    for i, j in dict_country.items():
        for k in j:
            if k == city:
                print(i)

check_country(city)



