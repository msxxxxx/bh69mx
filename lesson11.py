from abc import ABC, abstractmethod
from io import TextIOWrapper
from typing import Type, List, TypeVar

from pydantic import BaseModel, Field, PositiveInt
from pydantic.types import Decimal, PositiveFloat
from pydantic_core import ValidationError

Schema = TypeVar('Schema', bound=BaseModel)

# 1.	Написать Pydantic схему для валидации данных:
# a.	title - строка с длиной не более 128
# b.	description - строка с длиной не более 4096
# c.	price - Decimal 8/2
# d.	count - целое положительное число


class SchemaValid(BaseModel):
    title: str = Field(..., max_length=128)
    description: str = Field(..., max_length=4096)
    price: Decimal = Field(..., max_digits=8, decimal_places=2)
    count: PositiveInt



# 2.	Написать абстрактный класс:
# a.	schema - атрибут класса (объявляется с аннотацией типа без присваивания значения)
# b.	parse - метод класса принимающий объект файла, разделитель и список
# c.	dump - метод класса, принимающий список, объект файла и разделитель


class AbstractProducts(ABC):
    schema: Type[BaseModel]

    @classmethod
    @abstractmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        pass

    @classmethod
    @abstractmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
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
class Products(AbstractProducts):
    schema = SchemaValid

    @classmethod
    def parse(cls, file: TextIOWrapper, delimiter: str) -> List[Schema]:
        fieldnames = file.readline().strip().split(delimiter)
        values = [line.strip().split(delimiter) for line in file]
        values = [dict(zip(fieldnames, value)) for value in values]
        data = []
        for value in values:
            try:
                data.append(cls.schema(**value))
            except ValidationError:
                pass
        return data

    @classmethod
    def dump(cls, objs: List[Schema], file: TextIOWrapper, delimiter: str) -> None:
        objs = [obj.model_dump() for obj in objs]
        fieldnames = delimiter.join(objs[0].keys())
        objs = [delimiter.join(f'{value}' for value in obj.values()) for obj in objs]
        objs.insert(0, fieldnames)
        file.write('\n'.join(objs))


with open('products.csv', 'r', encoding='utf-8') as file, open('pr_output.csv', 'w', encoding='utf-8') as file2:  # type: TextIOWrapper
    Products.dump(Products.parse(file=file, delimiter=','), file=file2, delimiter=',')
