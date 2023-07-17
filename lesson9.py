# TODO Написать класс ConfigParser, конструктор класса принимает строку в формате:
text = '''
[Section1]
key1=value1
key2=value2
[Section2]
key3=value3
key4=value4
'''
# TODO написать метод класса loads, который будет вызываться в конструкторе, данный метод
#  принимает данную строку и преобразовывает в словарь словарей
#  результат метода после вызова в конструкторе, помещается в атрибут объекта data
# data = {
#     'Section1': {
#         'key1': 'value1',
#         'key2': 'value2',
#     },
#     'Section2': {
#         'key3': 'value3',
#         'key4': 'value4'
#     }
# }

class ConfigParser:

    def __int__(self, text: str) -> None:
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
        except KeyError:
            raise ValueError




