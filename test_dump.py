def dict_to_string(city_dict):
    result = ""
    #print(city_dict.items())
    for key, value in city_dict.items():
        for i,j in value.items():
            result += f"[{key}]\n{i}={j}\n"
        # result += f"{[key]}\n{value}\n"
        # for it in value:
        #     print(it)
    return result

city_dict = {
    'Section1': {'key1': 'value1', 'key2': 'value2'},
    'Section2': {'key3': 'value3', 'key4': 'value4'}
}

custom_str = dict_to_string(city_dict)
print(custom_str)