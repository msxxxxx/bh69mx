from pydantic import (
    BaseModel,
    Field,
    field_validator
)
from pydantic.types import Decimal, PositiveInt
from typing import List

# 1.	Написать Pydantic схему для валидации данных:
# a.	title - строка с длиной не более 128
# b.	description - строка с длиной не более 4096
# c.	price - Decimal 8/2
# d.	count - целое положительное число

class SchemaValid(BaseModel):
    title: str
    descr: str
    price: Decimal = Field(max_digits=8, decimal_places=2)
    count: PositiveInt

# city = SchemaValid.model_validate(file)
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

# 2.	Написать абстрактный класс:
# a.	schema - атрибут класса (объявляется с аннотацией типа без присваивания значения)
# b.	parse - метод класса принимающий объект файла, разделитель и список
# c.	dump - метод класса, принимающий список, объект файла и разделитель
from abc import ABC, abstractmethod
class AbstractProducts(ABC):
    schema: List[SchemaValid]
    def __init__(self, file, delimiter):
        self.file = file
        self.delimiter = delimiter

    def parse(self):
        pass

    # @abstractmethod
    def dump(self):
        pass

# 3.	На основании абстрактного класса из пункта 2, создать дочерний класс:
# a.	schema - присвоить в качестве значения ссылку на Pydantic схему из пункта 1
# b.	parse - реализовать метод класса, принимающий объект файла CSV, разделить,
# и возвращающий список экземпляром класса указанного в атрибуте класса schema.
# Если какая-то запись в файл не валидна - игнорировать
# c.	dump - метод класса, принимающий список экземпляров
# Pydantiс схемы, объект файла и разделитель и записывающий
# данные из схем в csv файл (все схемы в списке должны быть экземплярами
# схемы указанной в атрибуте класса schema, если одна из схем не является, вызывать исключение TypeError)
list_of_dictionaries = []
class Products(AbstractProducts):
    schema: SchemaValid

    def parse(self):

        with open(self.file) as infile:
            column_names = infile.readline()
            keys = column_names.strip().split(self.delimiter)
            number_of_columns = len(keys)
            data = infile.readlines()
            list_of_rows = []
            for row in data:
                list_of_rows.append(row.strip().split(self.delimiter))
            infile.close()
            for item in list_of_rows:
                row_as_a_dictionary = {}
                for i in range(number_of_columns):
                    row_as_a_dictionary[keys[i]] = item[i]
                list_of_dictionaries.append(row_as_a_dictionary)
        for items in list_of_dictionaries:
            try:
                s = SchemaValid(**items)
            except:
                pass

    def dumps(self, list_of_dictionaries):
        with open(self.file, 'w') as f:
            f.write(self.delimiter.join(list_of_dictionaries[0].keys()))
            f.write('\n')
            for row in list_of_dictionaries:
                f.write(self.delimiter.join(str(x) for x in row.values()))
                f.write('\n')
        return True

b = Products(file="products.csv", delimiter=',').parse()
lol = Products(file="pr_output.csv", delimiter=',').dumps(list_of_dictionaries=list_of_dictionaries)
