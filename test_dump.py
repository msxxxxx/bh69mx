def dict_to_string(text_dict):
    ss = ''
    for key, value in text_dict.items():
        t = str(key)
        z = ''
        for i, j in value.items():
            # print(i,j)
            z += f"\n{i}={j}"
        ss += str(f'[{t}]{z}\n')
    return ss

text_dict = {
    'Section1': {'key1': 'value1', 'key2': 'value2'},
    'Section2': {'key3': 'value3', 'key4': 'value4'},
    'Section3': {'key3': 'value3', 'key4': 'value4'},
    'Section4': {'key3': 'value3', 'key4': 'value4'},
    'Section5': {'key3': 'value3', 'key4': 'value4'},
    'Section6': {'key3': 'value3', 'key4': 'value4'}
}

custom_str = dict_to_string(text_dict)
print(custom_str)