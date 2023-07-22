from csv import reader, DictReader, writer, DictWriter
from pydantic import (
    BaseModel,
    EmailStr,
    PostgresDsn,
    Field,
    field_validator,
    model_validator,
    validate_call, ValidationError, PositiveInt
)
from pydantic.types import Decimal, PositiveInt

# 1.	Написать Pydantic схему для валидации данных:
# a.	title - строка с длиной не более 128
# b.	description - строка с длиной не более 4096
# c.	price - Decimal 8/2
# d.	count - целое положительное число

class Products(BaseModel):
    title: str
    descr: str
    price: Decimal = Field(max_digits=8, decimal_places=2)
    count: PositiveInt

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if len(value) > 128:
            raise ValueError("Not much 128 symbols")
        return value

    @field_validator("descr")
    @classmethod
    def validate_descr(cls, value):
        if len(value) > 4096:
            raise ValueError("Not much 4096 symbols")
        return value

    @field_validator("price")
    @classmethod
    def validate_price(cls, value: Decimal = Field(max_digits=8, decimal_places=2)):
        return value

    @field_validator("count")
    @classmethod
    def validate_count(cls, value: PositiveInt):
        return value


with open('products.csv', 'r', encoding='utf-8') as file:
    r = DictReader(file, delimiter=',')
    # for line in r:
    #     line = dict(line)
    #     a = Products(**line)
    #     print(a)

# 2.	Написать абстрактный класс:
# a.	schema - атрибут класса (объявляется с аннотацией типа без присваивания значения)
# b.	parse - метод класса принимающий объект файла, разделитель и список
# c.	dump - метод класса, принимающий список, объект файла и разделитель

class Abstrat:
    def __init__(self):
        self.schema: dict

    def parse(self, file, delimiter, lst):
        pass

    def dump(self, lst, file, delimiter):
        pass

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

# 3.	На основании абстрактного класса из пункта 2, создать дочерний класс:
# a.	schema - присвоить в качестве значения ссылку на Pydantic схему из пункта 1
# b.	parse - реализовать метод класса, принимающий объект файла CSV, разделить,
# и возвращающий список экземпляром класса указанного в атрибуте класса schema.
# Если какая-то запись в файл не валидна - игнорировать
# c.	dump - метод класса, принимающий список экземпляров
# Pydantiс схемы, объект файла и разделитель и записывающий
# данные из схем в csv файл (все схемы в списке должны быть экземплярами
# схемы указанной в атрибуте класса schema, если одна из схем не является, вызывать исключение TypeError)

class Children(Abstrat):
    schema = Products()

    def parse(self, file, delimiter):
        return self.schema

    def dump(self, lst, file, delimiter):
        return lst, file, delimiter



