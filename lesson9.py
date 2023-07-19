text = '''
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
'''
class ConfigParser:
    def __init__(self, text: str) -> None:
        self.data = self.loads(text)
    @classmethod
    def loads(cls, text: str) -> dict[str, dict[str, str]]:
        lines = [line for line in text.split('\n') if line]
        data = {}
        current_section = ''
        for line in lines:
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                data[current_section] = {}
            else:
                key, value = line.split('=')
                data[current_section][key] = value
        return data

    def has_section(self, section: str) -> bool:
        return section in self.data

    def has_param(self, section: str, param: str) -> bool:
        try:
            return param in self.data[section]
            #print(self.data[section].values())
        except KeyError:
            raise ValueError

#  3. объявить метод add_section принимающий название новой секции и объявляющий ее
#  в случае отсутствия, если такая секция уже есть, вызвать исключение ValueError
    def add_section(self, section: str):
        try:
            if section not in self.data:
            #     return True
            # else:
            #     return param in self.data[section] = section
            #     return data
            #     print(self.data[section])
                self.data[section] = {'key5': 'value5', 'key6': 'value6'}
                return self.data
            else:
                raise ValueError
        except KeyError:
            raise ValueError

#  5. объявить метод del_section - принимающий название секции и удаляющий ее, если секции
#  нет, ничего происходить не должно

    def del_section(self, section: str):
        try:
            if section in self.data:
            #     return True
            # else:
            #     return param in self.data[section] = section
            #     return data
            #     print(self.data[section])
                del self.data[section]
                return self.data
            else:
                return self.data
        except KeyError:
            raise ValueError

#  6. объявить метод del_param - принимающий название секции и название параметра
#  если данной секции нет - ValueError
#  если параметра в секции нет - ничего не происходит
#  если параметр в секции есть - удалить его 3

    def del_param(self, section: str, param: str):
        try:
            if param in self.data[section]:
                del self.data[section][param]
                return self.data
            else:
                return self.data
        except KeyError:
            raise ValueError

# print(ConfigParser.loads(text))
# print(ConfigParser(text=text).has_section(section='Section1'))
# print(ConfigParser(text=text).has_param(section='Section1', param='key1'))
#print(ConfigParser(text=text).add_section(section='Section4'))
#print(ConfigParser(text=text).del_section(section='Section1'))
print(ConfigParser(text=text).del_param(section='Section1', param='key1'))








