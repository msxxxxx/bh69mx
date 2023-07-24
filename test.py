def parse(fileName, delimiter):
    with open(fileName) as infile:
        column_names = infile.readline()
        keys = column_names.strip().split(delimiter)
        number_of_columns = len(keys)
        list_of_dictionaries = []
        data = infile.readlines()
        list_of_rows = []
        for row in data:
            list_of_rows.append(row.strip().split(delimiter))
        infile.close()
        for item in list_of_rows:
            row_as_a_dictionary = {}
            for i in range(number_of_columns):
                row_as_a_dictionary[keys[i]] = item[i]
            list_of_dictionaries.append(row_as_a_dictionary)
        return list_of_dictionaries
        # запихнуть валидатор a = Schema(**line)

    # for i in range(len(list_of_dictionaries)):
    #     print(list_of_dictionaries[i])

a = parse(fileName="products.csv", delimiter=',')
print(a)
lst = [{'title': 'banan', 'descr': 'fruit', 'price': '3.34', 'count': '10'}, {'title': 'orange', 'descr': 'fruit', 'price': '4.33', 'count': '20'}, {'title': 'limon', 'descr': 'fruit', 'price': '4.35', 'count': '5'}]
def dumps(fileName, delimiter, lst_of_dictionaries):
    with open(fileName, 'w') as f:
        f.write(delimiter.join(lst_of_dictionaries[0].keys()))
        f.write('\n')
        for row in lst_of_dictionaries:
            f.write(delimiter.join(str(x) for x in row.values()))
            f.write('\n')
    return True

b = dumps(fileName="pr_output.csv", delimiter=',', lst_of_dictionaries=lst)
print(b)